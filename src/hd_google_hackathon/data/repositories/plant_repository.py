from abc import ABC, abstractmethod
from typing import Optional

from hd_google_hackathon.domain.plant import Plant

class PlantRepository(ABC):
    @abstractmethod
    def get_plant_by_id(self, plant_id: str, tenant_id: str) -> Optional[Plant]:
        pass
