from selenium.webdriver.common.by import By


class MenuPage:

    # ---------- Locators ----------
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # ---------- Constructor ----------
    def __init__(self, driver):
        self.driver = driver

    # ---------- Actions ----------
    def open_menu(self):
        self.driver.find_element(*self.MENU_BUTTON).click()

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_LINK).click()

    def logout(self):
        self.open_menu()
        self.click_logout()