from __future__ import annotations

from pathlib import Path
import sys
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from tests.mocks.mock_order_repository import MockOrderRepository
from tests.mocks.mock_product_repository import MockProductRepository
from tests.mocks.mock_dealer_repository import MockDealerRepository
from tests.mocks.mock_plant_repository import MockPlantRepository
from tests.mocks.mock_component_repository import MockComponentRepository

@pytest.fixture
def order_repository() -> MockOrderRepository:
    """Provides a mock order repository."""
    return MockOrderRepository()


@pytest.fixture
def product_repository() -> MockProductRepository:
    """Provides a mock product repository."""
    return MockProductRepository()


@pytest.fixture
def dealer_repository() -> MockDealerRepository:
    """Provides a mock dealer repository."""
    return MockDealerRepository()


@pytest.fixture
def plant_repository() -> MockPlantRepository:
    """Provides a mock plant repository."""
    return MockPlantRepository()


@pytest.fixture
def component_repository() -> MockComponentRepository:
    """Provides a mock component repository."""
    return MockComponentRepository()