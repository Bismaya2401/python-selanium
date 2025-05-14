from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def place_order(self, country="India"):
        self.driver.find_element(By.ID, "country").send_keys("ind")
        suggestion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='suggestions']/ul/li/a[contains(text(), '{country}')]"))
        )
        suggestion.click()
        self.driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "alert-success").text
