import pytest
from playwright.sync_api import expect
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

URL = "https://automationteststore.com/"
VALID_USERNAME = "csaba.kelemen"
VALID_PASSWORD = "tesztteszt1"

def test_invalid_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(URL)
    login = LoginPage(page)
    login.goto_login()
    login.login('invaliduser', 'invalidpass')
    assert "Error" in login.get_login_error()

def test_valid_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(URL)
    login = LoginPage(page)
    login.goto_login()
    login.login(VALID_USERNAME, VALID_PASSWORD)
    assert login.is_on_my_account()

def test_direct_add_to_cart_from_datasheet(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(URL)
    prod = Product(page)
    cart = Cart(page)
    prod.search("Lipstick")
    prod.add_to_cart_from_datasheet()
    assert cart.is_checkout_available()

def test_add_to_cart_from_result_grid(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(URL)
    prod = Product(page)
    cart = Cart(page)
    prod.search("Lip")
    prod.click_product_title("Viva Glam Lipstick")
    prod.add_to_cart_from_datasheet()
    assert cart.is_checkout_available()

def test_no_product_found(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(URL)
    prod = Product(page)
    prod.search("dsadfsadsa")
    assert prod.is_no_product_found()

def test_checkout_and_order(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(URL)
    cart = Cart(page)
    cart.goto_checkout_header()
    cart.page.wait_for_selector('button#checkout_btn', timeout=20000)
    cart.click_confirm_order()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=20000)
    assert "checkout/success" in page.url

def test_empty_cart_checkout(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(URL)
    cart = Cart(page)
    cart.goto_checkout_header()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=20000)
    assert cart.is_cart_empty()