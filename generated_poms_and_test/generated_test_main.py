import pytest
from playwright.sync_api import expect

from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

BASE_URL = "https://automationteststore.com/"

def test_login_with_invalid_credentials(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL)
    login = LoginPage(page)
    login.click_login_or_register()
    login.fill_login_name("wronguser")
    login.fill_password("wrongpass")
    login.click_login_button()
    assert login.is_login_error_visible(), "Login error message should be visible"

def test_login_with_valid_credentials(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL)
    login = LoginPage(page)
    login.click_login_or_register()
    login.fill_login_name("csaba.kelemen")
    login.fill_password("tesztteszt1")
    login.click_login_button()
    assert login.is_my_account_visible(), "Logoff link should be visible on My Account"

def test_search_lipstick_and_add_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    product = Product(page)
    cart = Cart(page)
    page.goto(BASE_URL)
    product.fill_search_bar("Lipstick")
    product.press_enter_search()
    product.click_add_to_cart_from_details()
    assert cart.is_checkout_button_visible(), "Checkout button should be visible in cart"

def test_search_lip_and_add_viva_glam_lipstick_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    product = Product(page)
    cart = Cart(page)
    page.goto(BASE_URL)
    product.fill_search_bar("Lip")
    product.press_enter_search()
    product.click_product_by_title("Viva Glam Lipstick")
    product.click_add_to_cart_from_details()
    assert cart.is_checkout_button_visible(), "Checkout button should be visible in cart"

def test_search_nonsense_no_result(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    product = Product(page)
    page.goto(BASE_URL)
    product.fill_search_bar("dsadfsadsa")
    product.press_enter_search()
    assert product.is_no_products_message_visible(), "No products matching text should appear"

def test_checkout_confirm_order_success(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    cart = Cart(page)
    page.goto(BASE_URL)
    # Click Checkout from header (first a.menu_checkout)
    page.wait_for_selector('a.menu_checkout', timeout=10000)
    page.click('a.menu_checkout')
    cart.is_confirm_order_button_visible()
    cart.click_confirm_order_button()
    # Wait for possible redirect and check url
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=20000)
    assert "checkout/success" in page.url

def test_checkout_cart_empty(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    cart = Cart(page)
    page.goto(BASE_URL)
    # Click Checkout from header (first a.menu_checkout)
    page.wait_for_selector('a.menu_checkout', timeout=10000)
    page.click('a.menu_checkout')
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=20000)
    assert cart.is_cart_empty_message_visible(), "Cart should display empty message"