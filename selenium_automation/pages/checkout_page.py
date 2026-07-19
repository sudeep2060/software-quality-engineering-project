from selenium.webdriver.common.by import By


class CheckoutPage:

    # -------- Locators --------
    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    # -------- Constructor --------
    def __init__(self, driver):
        self.driver = driver

    # -------- Actions --------
    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def enter_first_name(self, firstname):
        self.driver.find_element(*self.FIRST_NAME).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.LAST_NAME).send_keys(lastname)

    def enter_postal_code(self, postal):
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def complete_checkout(self, firstname, lastname, postal):
        self.click_checkout()
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_postal_code(postal)
        self.click_continue()
        self.click_finish()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text