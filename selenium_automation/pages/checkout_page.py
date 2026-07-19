from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_checkout(self):
        checkout = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkout
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

        self.wait.until(
            EC.url_contains("checkout-step-one")
        )

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

    def enter_first_name(self, firstname):
        field = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME)
        )

        self.driver.execute_script("arguments[0].focus();", field)
        field.clear()
        field.send_keys(firstname)

        self.wait.until(
            lambda d: field.get_attribute("value") == firstname
        )

    def enter_last_name(self, lastname):
        field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )

        self.driver.execute_script("arguments[0].focus();", field)
        field.clear()
        field.send_keys(lastname)

        self.wait.until(
            lambda d: field.get_attribute("value") == lastname
        )

    def enter_postal_code(self, postal):
        field = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE)
        )

        self.driver.execute_script("arguments[0].focus();", field)
        field.clear()
        field.send_keys(postal)

        self.wait.until(
            lambda d: field.get_attribute("value") == postal
        )

    def click_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            continue_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        errors = self.driver.find_elements(*self.ERROR_MESSAGE)
        if errors:
            raise AssertionError(errors[0].text)

        self.wait.until(
            EC.url_contains("checkout-step-two")
        )

        self.wait.until(
            EC.visibility_of_element_located(self.FINISH_BUTTON)
        )

    def click_finish(self):
        finish = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            finish
        )

        self.driver.execute_script(
            "arguments[0].click();",
            finish
        )

        self.wait.until(
            EC.url_contains("checkout-complete")
        )

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

    def complete_checkout(self, firstname, lastname, postal):
        self.click_checkout()

        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_postal_code(postal)

        # Debug output for GitHub Actions
        print("===== FIELD VALUES =====")
        print("First Name:", self.driver.find_element(*self.FIRST_NAME).get_attribute("value"))
        print("Last Name :", self.driver.find_element(*self.LAST_NAME).get_attribute("value"))
        print("Postal    :", self.driver.find_element(*self.POSTAL_CODE).get_attribute("value"))
        print("========================")

        self.click_continue()
        self.click_finish()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text