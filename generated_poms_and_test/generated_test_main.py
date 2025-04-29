# test_generated_shop.py
import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

BASE_URL = "https://automationteststore.com/"

@pytest.mark.usefixtures("set_up_fresh_browser")
def test_unsuccessful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_login_header()
    login_page.fill_username("invalid_user")
    login_page.fill_password("invalid_password")
    login_page.click_login_button()
    assert login_page.error_message_is_visible()

@pytest.mark.usefixtures("set_up_fresh_browser")
def test_successful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_login_header()
    login_page.fill_username("csaba.kelemen")
    login_page.fill_password("tesztteszt1")
    login_page.click_login_button()
    cart = Cart(page)
    assert cart.my_account_heading_is_visible()

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_search_lipstick_and_add_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_search_bar()
    login_page.enter_keyword_and_press_enter("Lipstick")
    product = Product(page)
    product.click_add_to_cart_on_datasheet()
    cart = Cart(page)
    assert cart.checkout_button_visible()

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_search_lip_in_grid_and_add_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_search_bar()
    login_page.enter_keyword_and_press_enter("Lip")
    product = Product(page)
    product.click_viva_glam_lipstick_in_results()
    product.click_add_to_cart_on_datasheet()
    cart = Cart(page)
    assert cart.checkout_button_visible()

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_search_no_finding(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_search_bar()
    login_page.enter_keyword_and_press_enter("dsadfsadsa")
    product = Product(page)
    assert product.no_results_div_visible()

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_checkout_and_confirm_order(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_top_menu_checkout()
    cart = Cart(page)
    assert cart.confirm_order_button_visible()
    cart.click_confirm_order_button()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=30000)
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/success"

@pytest.mark.usefixtures("set_up_logged_in_browser")
def test_checkout_when_cart_empty(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL, timeout=30000)
    login_page = LoginPage(page)
    login_page.click_top_menu_checkout()
    cart = Cart(page)
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=30000)
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/cart"
    assert cart.empty_cart_visible()