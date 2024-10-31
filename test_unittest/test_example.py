import unittest
from components.ShoppingCart import ShoppingCart
from components.process import process_order


class TestShoppingCart(unittest.TestCase):
    def test_add_item(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add_to_cart("apple", 1.5)
        shopping_cart.add_to_cart("banana", 2.0)
        self.assertTrue(len(shopping_cart.items) == 2)
        self.assertFalse(len(shopping_cart.items) < 2)

    def test_calculate_total(self):
        shopping_cart = ShoppingCart()
        shopping_cart.add_to_cart("apple", 1.5)
        shopping_cart.add_to_cart("banana", 2.0)
        self.assertEqual(shopping_cart.calculate_total(), 3.5)

    def test_process_order_empty_cart(self):
        shopping_cart = ShoppingCart()
        with self.assertRaises(ValueError):
            process_order(shopping_cart)
