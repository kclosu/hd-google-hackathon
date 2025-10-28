"""Helpers for preparing callables to be exposed as ADK tools."""

from functools import wraps
from inspect import Signature, signature
from typing import Any, Callable


def _strip_bound_params(sig: Signature, bound_param_names: set[str]) -> Signature:
    """Return a signature without parameters that are being bound."""
    params = tuple(
        param
        for name, param in sig.parameters.items()
        if name not in bound_param_names
    )
    return sig.replace(parameters=params)


def bind_tool(func: Callable[..., Any], /, **bound_kwargs: Any) -> Callable[..., Any]:
    """Return ``func`` with ``bound_kwargs`` applied while keeping tool metadata intact."""

    bound_param_names = set(bound_kwargs)
    func_signature = signature(func)
    tool_signature = _strip_bound_params(func_signature, bound_param_names)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        conflicting = bound_param_names.intersection(kwargs)
        if conflicting:
            conflicts = ", ".join(sorted(conflicting))
            raise TypeError(f"Arguments already bound for: {conflicts}")

        merged_kwargs = {**kwargs, **bound_kwargs}
        return func(*args, **merged_kwargs)

    # Update annotations to reflect the exposed parameters only.
    if func.__annotations__:
        wrapper.__annotations__ = {
            name: annotation
            for name, annotation in func.__annotations__.items()
            if name == "return" or name not in bound_param_names
        }

    wrapper.__signature__ = tool_signature  # type: ignore[attr-defined]
    return wrapper
