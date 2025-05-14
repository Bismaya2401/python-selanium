from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, product_names):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "card-title"))
        )
        products = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")
        buttons = self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")

        for i, product in enumerate(products):
            if product.text in product_names:
                buttons[i].click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.nav-link.btn.btn-primary").click()
