from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
#login 
    def login_as_user(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[value='user']").click()
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, "okayBtn"))).click()
        except:
            pass
        Select(self.driver.find_element(By.TAG_NAME, "select")).select_by_visible_text("Student")
        self.driver.find_element(By.ID, "terms").click()
        self.driver.find_element(By.ID, "signInBtn").click()
