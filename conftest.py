import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Add screenshot on failure to allure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup_browser")
        if driver:
            screenshot_path = "screenshots/failure.png"
            driver.save_screenshot(screenshot_path)
            import allure
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
