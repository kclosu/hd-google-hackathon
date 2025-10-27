"""Smoke tests for the mock data manager fixtures."""

import mock_data.data_manager as data_manager


def test_module_imports():
    # Importing the module should expose the basic helper functions.
    expected = {
        "get_product_by_id",
        "get_component_by_id",
        "get_plant_by_id",
        "get_dealer_by_id",
        "get_dealer_product_by_id",
        "get_dealer_products_by_dealer",
        "get_order_by_id",
        "get_orders_by_dealer",
        "create_order",
        "update_order_status",
    }

    assert expected.issubset(set(dir(data_manager)))
