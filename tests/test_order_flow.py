import pytest
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.epic("E2E Order Flow")
@allure.feature("Purchase")
@allure.story("Place order successfully")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_e2e_order_flow(setup_browser):
    driver = setup_browser
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Login to app"):
        login.login_as_user("rahulshettyacademy", "learning")

    with allure.step("Add items to cart"):
        product.add_products_to_cart(["iphone X", "Samsung Note 8"])
        product.go_to_cart()

    with allure.step("Verify and checkout cart"):
        cart.verify_cart_items(["iphone X", "Samsung Note 8"])
        cart.proceed_to_checkout()

    with allure.step("Place order and confirm"):
        checkout.place_order()
        success_message = checkout.get_success_message()
        assert "Success! Thank you!" in success_message
