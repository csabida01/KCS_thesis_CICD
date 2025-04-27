import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart
import time

@pytest.mark.usefixtures("set_up_fresh_browser")
def test_unsuccessful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    login = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login.goto_login()
    login.login("invaliduser", "invalidpass")
    assert login.check_login_error() is True

@pytest.mark.usefixtures("set_up_fresh_browser")
def test_successful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    login = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login.goto_login()
    login.login("csaba.kelemen", "tesztteszt1")
    # Check some "my account" locator after login (from Update and checkout header, without using URL)
    page.wait_for_selector('a#cart_checkout1', timeout=15000)
    assert page.is_visible('a#cart_checkout1')

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_add_to_cart_from_search_filled(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    product = Product()
    cart = Cart()
    page.goto("https://automationteststore.com/")
    login.fill_search_and_submit("Lipstick")
    # Directly on datasheet, add to cart
    Product.add_to_cart_from_datasheet(page)
    assert Cart.can_see_checkout(page)

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_add_to_cart_from_grid_then_details(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    product = Product()
    cart = Cart()
    page.goto("https://automationteststore.com/")
    login.fill_search_and_submit("Lip")
    Product.click_viva_glam_lipstick_from_search(page)
    Product.add_to_cart_from_datasheet(page)
    assert Cart.can_see_checkout(page)

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_search_with_no_results(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login.fill_search_and_submit("dsadfsadsa")
    assert Product.is_no_results_message(page)

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_checkout_and_confirm_order(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    cart = Cart()
    page.goto("https://automationteststore.com/")
    login.click_checkout_header()
    # Wait for Confirm Order to appear and then click
    Cart.do_confirm_order(page)
    assert Cart.is_order_success(page)

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_checkout_empty_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    cart = Cart()
    page.goto("https://automationteststore.com/")
    login.click_checkout_header()
    # url should change to cart
    page.wait_for_url('https://automationteststore.com/index.php?rt=checkout/cart', timeout=20000)
    assert Cart.is_cart_empty(page)