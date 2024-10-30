import pytest
from components.ShoppingCart import ShoppingCart

@pytest.fixture
def shopping_cart() -> ShoppingCart:
    return ShoppingCart()


def test_add_to_cart(shopping_cart):
    shopping_cart.add_to_cart("apple", 1.5)
    shopping_cart.add_to_cart("banana", 0.75)
    assert len(shopping_cart.items) == 2
    item1 = shopping_cart.items[0]
    item2 = shopping_cart.items[1]
    assert item1.get("item") == "apple" and item1.get("price") == 1.5
    assert item2.get("item") == "banana" and item2.get("price") == 0.75
