## Gemini Workflow Notes

Use `uv` to manage dependencies and isolated tooling for the project:

```bash
uv sync --extra dev
```

Run project entry points and tests through `uv run` so they execute inside the synced environment:

```bash
uv run python main.py
uv run pytest
```

For a quick feedback loop, exercise changes with the existing pytest suite:

1. Start with failing coverage by running `uv run pytest`.
2. Inspect failures to understand regressions or missing coverage.
3. Adjust implementation or tests as needed.
4. Repeat `uv run pytest` until the suite passes cleanly.

If you need a traditional virtual environment (e.g., for debugging in an IDE), activate `.venv` after `uv sync` (`.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Unix).

Favor a lightweight test-driven approach: sketch the test (or extend an existing one) that captures the expected behavior, watch it fail, implement the fix, and rerun until green to keep changes disciplined and observable.
