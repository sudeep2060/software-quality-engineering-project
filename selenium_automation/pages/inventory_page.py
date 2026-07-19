from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.wait = WebDriverWait(driver, 10)

    # -------- Actions --------
    def add_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )

    def remove_backpack(self):
        remove = self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BACKPACK)
        )

        self.driver.execute_script("arguments[0].click();", remove)

        self.wait.until(
            EC.invisibility_of_element_located(self.CART_BADGE)
        )

    def open_cart(self):
        cart = self.wait.until(
        EC.element_to_be_clickable(self.CART_ICON)
    )

        cart.click()

        self.wait.until(
        EC.url_contains("cart.html")
    )

        self.wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    # -------- Get Information --------
    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    def get_first_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    # -------- Verification --------
    def is_cart_badge_displayed(self):
        return len(self.driver.find_elements(*self.CART_BADGE)) > 0