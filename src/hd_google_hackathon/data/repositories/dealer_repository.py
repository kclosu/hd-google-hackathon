from abc import ABC, abstractmethod
from typing import Optional

from hd_google_hackathon.domain.dealer import Dealer

class DealerRepository(ABC):
    @abstractmethod
    def get_dealer_by_id(self, dealer_id: str, tenant_id: str) -> Optional[Dealer]:
        pass
