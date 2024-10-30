from components.ShoppingCart import ShoppingCart
from typing import Dict

def process_order(cart: ShoppingCart) -> Dict:
    if len(cart.items) == 0:
        raise ValueError("Carrinho está vazio!")
    return {"status": "success", "total": cart.calculate_total()}
