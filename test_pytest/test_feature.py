import pytest
from components.ShoppingCart import ShoppingCart


@pytest.fixture
def shopping_cart() -> ShoppingCart:
    return ShoppingCart()


def test_shopping_cart(shopping_cart):
    shopping_cart.add_to_cart("item1", 10)
    shopping_cart.add_to_cart("item2", 20)
    shopping_cart.add_to_cart("item3", 30)
    assert len(shopping_cart.items) == 3
    assert shopping_cart.calculate_total() == 60
