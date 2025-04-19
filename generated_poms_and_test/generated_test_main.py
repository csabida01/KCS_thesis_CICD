import pytest
from playwright.sync_api import expect

from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

BASE_URL = 'https://automationteststore.com/'

# 1. Login fail
def test_login_fail(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    login_page.goto_login()
    login_page.do_login("notauser", "wrongpassword")
    assert login_page.is_error_message_visible()

# 2. Login success
def test_login_success(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    login_page.goto_login()
    login_page.do_login("csaba.kelemen", "tesztteszt1")
    assert login_page.is_account_dashboard_visible()

# 3. Search "Lipstick", add to cart from datasheet, see checkout btn
def test_search_lipstick_add_to_cart_direct(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    product = Product(page)
    cart = Cart(page)
    product.search_product("Lipstick")
    product.click_add_to_cart_datasheet()
    assert cart.is_checkout_btn_visible()

# 4. Search "Lip", click Viva Glam Lipstick, add to cart, see checkout btn
def test_search_lip_click_viva_glam_add_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    product = Product(page)
    cart = Cart(page)
    product.search_product("Lip")
    product.click_result_by_title("Viva Glam Lipstick")
    product.click_add_to_cart_datasheet()
    assert cart.is_checkout_btn_visible()

# 5. Search for nonsense, get no results
def test_search_nonsense_no_results(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    product = Product(page)
    product.search_product("dsadfsadsa")
    assert product.is_no_results_message_visible()

# 6. Checkout flow, confirm order, check order processed url
def test_checkout_confirm_order_success(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    cart = Cart(page)
    cart.goto_checkout()
    cart.wait_for_confirm_order_btn()
    cart.click_confirm_order()
    page.wait_for_url(lambda url: url == cart.success_url, timeout=20000)
    assert cart.current_url() == cart.success_url

# 7. Checkout with empty cart shows empty cart
def test_checkout_with_empty_cart_shows_message(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    cart = Cart(page)
    cart.goto_checkout()
    page.wait_for_url(lambda url: url == cart.cart_url, timeout=10000)
    assert cart.current_url() == cart.cart_url
    assert cart.is_cart_empty_message_visible()