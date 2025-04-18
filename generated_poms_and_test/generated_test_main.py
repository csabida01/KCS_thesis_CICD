import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart
import time

BASE_URL = "https://automationteststore.com/"

def goto_main_page(page):
    page.goto(BASE_URL, timeout=60000)

@pytest.mark.flaky(reruns=1)
def test_unsuccessful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    goto_main_page(page)
    login_page = LoginPage(page)
    login_page.click_login_or_register()
    login_page.fill_username("wrong.username")
    login_page.fill_password("wrongpassword")
    login_page.click_login_button()
    assert login_page.is_error_message_visible()

@pytest.mark.flaky(reruns=1)
def test_successful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    goto_main_page(page)
    login_page = LoginPage(page)
    login_page.click_login_or_register()
    login_page.fill_username("csaba.kelemen")
    login_page.fill_password("tesztteszt1")
    login_page.click_login_button()
    cart = Cart(page)
    assert cart.is_my_account_page_visible()

@pytest.mark.flaky(reruns=1)
def test_add_lipstick_direct_datasheet(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    goto_main_page(page)
    product = Product(page)
    product.search_for_product("Lipstick")
    product.click_add_to_cart_from_datasheet()
    cart = Cart(page)
    assert cart.is_checkout_button_visible()

@pytest.mark.flaky(reruns=1)
def test_add_lipstick_from_search_grid(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    goto_main_page(page)
    product = Product(page)
    product.search_for_product("Lip")
    time.sleep(2)  # Allow for slow loading
    product.click_add_to_cart_from_grid_viva_glam_lipstick()
    cart = Cart(page)
    assert cart.is_checkout_button_visible()

@pytest.mark.flaky(reruns=1)
def test_search_nonsense_product(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    goto_main_page(page)
    product = Product(page)
    product.search_for_product("dsadfsadsa")
    assert product.is_no_product_found_message_visible()

@pytest.mark.flaky(reruns=1)
def test_checkout_confirm_order(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    goto_main_page(page)
    page.wait_for_selector('a.menu_checkout', timeout=15000)
    page.click('a.menu_checkout')
    cart = Cart(page)
    cart.click_confirm_order()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=20000)
    assert "checkout/success" in page.url

@pytest.mark.flaky(reruns=1)
def test_checkout_empty_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    goto_main_page(page)
    page.wait_for_selector('a.menu_checkout', timeout=15000)
    page.click('a.menu_checkout')
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=20000)
    assert "checkout/cart" in page.url