from pages.login_page import LoginPage


def test_inventory_page(driver):

    login = LoginPage(driver)

    login.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url