from selenium.webdriver.common.by import By


class InventoryPage:

    # -------- Locators --------
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    # -------- Constructor --------
    def __init__(self, driver):
        self.driver = driver

    # -------- Actions --------
    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def remove_backpack(self):
        self.driver.find_element(*self.REMOVE_BACKPACK).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    # -------- Get Information --------
    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def get_first_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text

    # -------- Verification --------
    def is_cart_badge_displayed(self):
        return len(self.driver.find_elements(*self.CART_BADGE)) > 0