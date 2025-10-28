from typing import Optional

from hd_google_hackathon.data.repositories.component_repository import ComponentRepository
from hd_google_hackathon.domain.component import Component


class DummyComponentRepository(ComponentRepository):
    """This is a dummy implementation of the `ComponentRepository` that returns empty data."""

    def get_component_by_id(self, component_id: str, tenant_id: str) -> Optional[Component]:
        return None

    def get_component_stock(self, component_id: str, tenant_id: str) -> int:
        return 0
