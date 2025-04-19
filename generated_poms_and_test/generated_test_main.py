import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

# Tests 1 & 2 use `set_up_fresh_browser` (fresh context)
def test_login_invalid_credentials(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.login_or_register_link().click()
    login.loginname_input().wait_for(state="visible", timeout=8000)
    login.loginname_input().fill("baduser")
    login.password_input().fill("badpass")
    login.login_button().click()
    login.login_error_message().wait_for(state="visible", timeout=9000)
    assert login.login_error_message().is_visible()

def test_login_valid_credentials(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.login_or_register_link().click()
    login.loginname_input().wait_for(state="visible", timeout=8000)
    login.loginname_input().fill("csaba.kelemen")
    login.password_input().fill("tesztteszt1")
    login.login_button().click()
    login.account_dashboard().wait_for(state="visible", timeout=9000)
    assert login.account_dashboard().is_visible()

# Product and cart flows use set_up_logged_in_browser fixture
def test_product_search_and_cart_datasheet(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    prod = Product(page)
    cart = Cart(page)
    # 3rd test: search for "Lipstick", direct to data sheet, add to cart, see checkout button
    login.search_bar_input().click()
    login.search_bar_input().fill("Lipstick")
    login.search_bar_input().press("Enter")
    prod.add_to_cart_data_sheet().wait_for(state="visible", timeout=9000)
    prod.add_to_cart_data_sheet().click()
    cart.checkout_button().wait_for(state="visible", timeout=9000)
    assert cart.checkout_button().is_visible()

def test_product_search_grid_and_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    prod = Product(page)
    cart = Cart(page)
    # 4th test: search for Lip, click Viva Glam Lipstick, add to cart, see checkout button
    login.search_bar_input().click()
    login.search_bar_input().fill("Lip")
    login.search_bar_input().press("Enter")
    prod.viva_glam_lipstick_link().wait_for(state="visible", timeout=9000)
    prod.viva_glam_lipstick_link().click()
    prod.add_to_cart_data_sheet().wait_for(state="visible", timeout=9000)
    prod.add_to_cart_data_sheet().click()
    cart.checkout_button().wait_for(state="visible", timeout=9000)
    assert cart.checkout_button().is_visible()

def test_search_yields_no_result(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    prod = Product(page)
    # 5th test: nonsense search, check 'no product' div
    login.search_bar_input().click()
    login.search_bar_input().fill("dsadfsadsa")
    login.search_bar_input().press("Enter")
    prod.no_product_found_msg().wait_for(state="visible", timeout=9000)
    assert prod.no_product_found_msg().is_visible()

def test_checkout_and_confirm_order(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    cart = Cart(page)
    # 6th test: Checkout menu top, confirm button, confirm URL
    login.top_checkout_link().click()
    cart.confirm_order_button().wait_for(state="visible", timeout=11000)
    cart.confirm_order_button().click()
    page.wait_for_url('https://automationteststore.com/index.php?rt=checkout/success', timeout=12000)
    assert 'checkout/success' in page.url

def test_checkout_cart_empty(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    cart = Cart(page)
    # 7th test: Click checkout top, check for empty cart URL
    login.top_checkout_link().click()
    page.wait_for_url('https://automationteststore.com/index.php?rt=checkout/cart', timeout=9000)
    assert 'checkout/cart' in page.url