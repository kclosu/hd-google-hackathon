from abc import ABC, abstractmethod
from typing import Optional

from hd_google_hackathon.domain.component import Component

class ComponentRepository(ABC):
    @abstractmethod
    def get_component_by_id(self, component_id: str, tenant_id: str) -> Optional[Component]:
        pass

    @abstractmethod
    def get_component_stock(self, component_id: str, tenant_id: str) -> int:
        pass
