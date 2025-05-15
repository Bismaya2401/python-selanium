import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import allure

@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    
    # ❗️REMOVE Linux-only line
    # options.binary_location = "/usr/bin/chromium-browser"  <-- REMOVE this

    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)  # This will now auto-detect your local Chrome
    yield driver
    driver.quit()

# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup_browser")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}_failure.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
