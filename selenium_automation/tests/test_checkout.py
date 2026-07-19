from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    checkout = CheckoutPage(driver)

    # Login
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory.add_backpack()

    # Open cart
    inventory.open_cart()

    # Checkout
    checkout.complete_checkout(
        "Sudeep",
        "Bhattarai",
        "44600"
    )

    # Verify order success
    assert checkout.get_success_message() == "Thank you for your order!"