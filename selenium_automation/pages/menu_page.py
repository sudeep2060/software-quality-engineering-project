from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_menu(self):
        menu = self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )

        self.driver.execute_script("arguments[0].click();", menu)

        self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_LINK)
        )

    def click_logout(self):
        logout = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )

        self.driver.execute_script("arguments[0].click();", logout)

        self.wait.until(
            EC.url_contains("saucedemo.com")
        )

    def logout(self):
        self.open_menu()
        self.click_logout()