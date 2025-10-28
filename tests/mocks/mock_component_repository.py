from typing import Optional

from hd_google_hackathon.data.repositories.component_repository import ComponentRepository
from hd_google_hackathon.domain.component import Component

from .data.components import components as MOCK_COMPONENTS


class MockComponentRepository(ComponentRepository):
    """This is a mock implementation of the `ComponentRepository` that uses a dictionary for storage."""

    def __init__(self) -> None:
        self._components: Dict[str, Component] = {component.id: component for component in MOCK_COMPONENTS}

    def get_component_by_id(self, component_id: str, tenant_id: str) -> Optional[Component]:
        """This method retrieves a component by its ID."""
        # The tenant_id is not used in this mock implementation.
        return self._components.get(component_id)

    def get_component_stock(self, component_id: str, tenant_id: str) -> int:
        """This method retrieves the stock of a component by its ID."""
        # The tenant_id is not used in this mock implementation.
        component = self._components.get(component_id)
        return component.stock if component else 0
