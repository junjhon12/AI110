import pytest
from models import Drinks, Main, ItemCollection, Transaction

def test_calculate_total_with_multiple_items():
    """
    Logic Test (Happy Path): Verify that adding multiple items correctly computes the total.
    """
    # Setup
    tx = Transaction()
    cola = Drinks(name="Cola", price=2.50, category="Drinks")
    burger = Main(name="Spicy Burger", price=8.50, category="Main")
    
    # Action
    tx.add_item(cola)
    tx.add_item(burger)
    
    # Assert
    assert tx.total == 11.00
    assert tx.compute_total() == 11.00

def test_order_total_is_zero_when_empty():
    """
    Edge Case: Verify that a new transaction with no items has a total of $0.0.
    """
    # Setup
    tx = Transaction()
    
    # Action
    total = tx.compute_total()
    
    # Assert
    assert total == 0.0
    assert tx.total == 0.0

def test_filter_by_category():
    """
    Logic Test: Verify that filtering by category only returns the matching items.
    """
    # Setup
    menu = ItemCollection()
    cola = Drinks(name="Cola", price=2.50, category="Drinks")
    water = Drinks(name="Water", price=1.00, category="Drinks")
    burger = Main(name="Spicy Burger", price=8.50, category="Main")
    
    menu.add(cola)
    menu.add(water)
    menu.add(burger)
    
    # Action
    drinks_only = menu.filter_by_category("Drinks")
    
    # Assert
    assert len(drinks_only) == 2
    assert cola in drinks_only
    assert water in drinks_only
    assert burger not in drinks_only