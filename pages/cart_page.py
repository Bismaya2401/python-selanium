from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_cart_items(self, expected_items):
        cart_items = self.driver.find_elements(By.XPATH, "//h4[@class='media-heading']/a")
        actual_items = [item.text for item in cart_items]
        assert actual_items == expected_items, f"Expected {expected_items}, got {actual_items}"

    def proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
