import pytest
from playwright.sync_api import expect
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

@pytest.mark.order(1)
def test_invalid_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.click_login_or_register()
    login.fill_username("incorrect_user")
    login.fill_password("badpassword")
    login.click_login_button()
    assert login.is_login_error_visible(), "Error message did not appear for invalid login"

@pytest.mark.order(2)
def test_successful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.click_login_or_register()
    login.fill_username("csaba.kelemen")
    login.fill_password("tesztteszt1")
    login.click_login_button()
    assert login.is_my_account_loaded(), "Account Dashboard was not visible after valid login"

@pytest.mark.order(3)
def test_search_and_add_to_cart_single_result(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    product = Product(page)
    cart = Cart(page)
    product.search_and_enter("Lipstick")
    product.click_add_to_cart_from_datasheet()
    assert cart.is_checkout_button_visible(), "Checkout button not visible after adding to cart from product page"

@pytest.mark.order(4)
def test_search_and_add_to_cart_from_grid(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    product = Product(page)
    cart = Cart(page)
    product.search_and_enter("Lip")
    product.select_lipstick_from_grid_by_title()
    product.click_add_to_cart_from_datasheet()
    assert cart.is_checkout_button_visible(), "Checkout button not visible after adding to cart from product grid"

@pytest.mark.order(5)
def test_search_no_results(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    product = Product(page)
    product.search_and_enter("dsadfsadsa")
    assert product.is_no_product_result_visible(), "No results message not found for nonsense search"

@pytest.mark.order(6)
def test_checkout_and_confirm_order_success(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    cart = Cart(page)
    cart.click_checkout_from_top()
    cart.click_confirm_order()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=20000)
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/success"

@pytest.mark.order(7)
def test_cart_empty_checkout(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    cart = Cart(page)
    cart.click_checkout_from_top()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=20000)
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/cart"