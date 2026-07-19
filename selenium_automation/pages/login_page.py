from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_username(self, username):
        field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        # Success login
        if username == "standard_user":
            self.wait.until(
                EC.visibility_of_element_located(
                    self.INVENTORY_CONTAINER
                )
            )
        # Invalid login
        else:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            )

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        ).text