from pages.login_page import LoginPage
from pages.menu_page import MenuPage


def test_valid_login(driver):
    login = LoginPage(driver)

    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login = LoginPage(driver)

    login.login("locked_out_user", "secret_sauce")

    assert "Epic sadface" in login.get_error_message()
    
def test_logout(driver):

    login = LoginPage(driver)
    menu = MenuPage(driver)

    login.login("standard_user", "secret_sauce")

    menu.logout()

    assert "saucedemo.com" in driver.current_url