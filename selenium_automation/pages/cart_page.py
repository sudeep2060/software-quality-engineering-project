def click_checkout(self):
    checkout = self.wait.until(
        EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
    )

    checkout.click()

    print("URL after checkout click:", self.driver.current_url)
    print("Page title:", self.driver.title)
    print("Checkout button still exists:", len(self.driver.find_elements(*self.CHECKOUT_BUTTON)))

    self.wait.until(
        EC.visibility_of_element_located(self.FIRST_NAME)
    )