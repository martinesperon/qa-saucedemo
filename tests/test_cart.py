# tests/test_cart.py

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time
import os

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
])
def test_add_to_cart(setup, username, password):
    driver = setup
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.login(username, password)

    # Agregar productos
    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]
    for item in items_to_add:
        inventory_page.add_item_to_cart_by_name(item)

    # Ir al carrito
    inventory_page.go_to_cart()

    # Validar que los ítems estén en el carrito
    items_in_cart = cart_page.get_cart_items()
    assert all(item in items_in_cart for item in items_to_add), f"Faltan productos en el carrito: {items_to_add} vs {items_in_cart}"

    # Validar cantidad
    assert len(items_in_cart) == 2

    # Esperar para ver el resultado
    time.sleep(1)
