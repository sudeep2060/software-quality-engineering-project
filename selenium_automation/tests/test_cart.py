from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()

    assert inventory.get_cart_count() == "1"


def test_open_cart(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()

    inventory.open_cart()

    assert "cart" in driver.current_url


def test_verify_product_name(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    assert inventory.get_first_product_name() == "Sauce Labs Backpack"


def test_remove_product(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()

    inventory.remove_backpack()

    assert inventory.is_cart_badge_displayed() is False


def test_cart_badge(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()
  
    assert inventory.is_cart_badge_displayed() is True