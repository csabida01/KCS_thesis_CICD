import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

BASE_URL = "https://automationteststore.com/"

def test_unsuccessful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)

    login_page.login_or_register()
    login_page.fill_login_name("invaliduser")
    login_page.fill_password("invalidpass")
    login_page.submit()
    assert "Incorrect login or password provided" in login_page.get_login_error()

def test_successful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)

    login_page.login_or_register()
    login_page.fill_login_name("csaba.kelemen")
    login_page.fill_password("tesztteszt1")
    login_page.submit()
    cart = Cart(page)
    assert cart.is_my_account_visible()

def test_add_lipstick_direct_and_checkout_button(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    product = Product(page)
    cart = Cart(page)

    login_page.search_for("Lipstick")
    # Product details page loaded, add to cart directly
    product.add_to_cart_from_details()
    assert cart.is_checkout_button_appears()

def test_search_lip_and_add_viva_glam(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    product = Product(page)
    cart = Cart(page)

    login_page.search_for("Lip")
    product.click_product_by_title("Viva Glam Lipstick")
    product.add_to_cart_from_details()
    assert cart.is_checkout_button_appears()

def test_search_for_nonexistent_product_returns_text(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    product = Product(page)

    nonsense = "dsadfsadsa"
    login_page.search_for(nonsense)
    assert "There is no product that matches the search criteria." in product.get_no_results_text()

def test_checkout_confirm_order_flow(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    cart = Cart(page)

    login_page.click_checkout_top_menu()
    cart.checkout_confirm_order()
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/success"

def test_checkout_leads_to_empty_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    cart = Cart(page)

    login_page.click_checkout_top_menu()
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/cart"