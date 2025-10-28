from typing import Optional

from hd_google_hackathon.data.repositories.dealer_repository import DealerRepository
from hd_google_hackathon.domain.dealer import Dealer

from .data.dealers import dealers as MOCK_DEALERS


class MockDealerRepository(DealerRepository):
    """This is a mock implementation of the `DealerRepository` that uses a dictionary for storage."""

    def __init__(self) -> None:
        self._dealers: Dict[str, Dealer] = {dealer.id: dealer for dealer in MOCK_DEALERS}

    def get_dealer_by_id(self, dealer_id: str, tenant_id: str) -> Optional[Dealer]:
        """This method retrieves a dealer by its ID."""
        # The tenant_id is not used in this mock implementation.
        return self._dealers.get(dealer_id)
