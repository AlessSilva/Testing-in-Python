import pytest
from components.ShoppingCart import ShoppingCart
from components.process import process_order


@pytest.fixture
def shopping_cart() -> ShoppingCart:
    return ShoppingCart()


def test_process_order_integration(shopping_cart):
    shopping_cart.add_to_cart("item1", 15)
    shopping_cart.add_to_cart("item2", 25)

    result = process_order(shopping_cart)
    assert result["status"] == "success"
    assert result["total"] == 40


def test_process_order_empty_cart(shopping_cart):

    with pytest.raises(ValueError) as exc_info:
        process_order(shopping_cart)
    assert str(exc_info.value) == "Carrinho está vazio!"
