from typing import Optional

from hd_google_hackathon.data.repositories.plant_repository import PlantRepository
from hd_google_hackathon.domain.plant import Plant

from .data.plants import plants as MOCK_PLANTS


class MockPlantRepository(PlantRepository):
    """This is a mock implementation of the `PlantRepository` that uses a dictionary for storage."""

    def __init__(self) -> None:
        self._plants: Dict[str, Plant] = {plant.id: plant for plant in MOCK_PLANTS}

    def get_plant_by_id(self, plant_id: str, tenant_id: str) -> Optional[Plant]:
        """This method retrieves a plant by its ID."""
        # The tenant_id is not used in this mock implementation.
        return self._plants.get(plant_id)
