import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

# --- 1. Unsuccessful login ---
def test_invalid_login_shows_error(set_up_fresh_browser):
    browser, page = set_up_fresh_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.goto_login_page()
    login.login("invalid_user", "invalid_pass")
    assert login.get_login_error() == "Error: Incorrect login or password provided."

# --- 2. Successful login and account details visible ---
def test_valid_login_my_account_visible(set_up_fresh_browser):
    browser, page = set_up_fresh_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.goto_login_page()
    login.login("csaba.kelemen", "tesztteszt1")
    cart = Cart(page)
    assert cart.account_edit_details_visible()

# --- 3. Search "Lipstick" (direct product), add to cart, verify checkout visible ---
def test_lipstick_direct_add_to_cart_checkout(cart: None, set_up_logged_in_browser):
    browser, page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.search("Lipstick")
    # On details page, add to cart:
    product = Product(page)
    product.add_to_cart()
    cart = Cart(page)
    assert cart.checkout_visible()

# --- 4. Search "Lip", select Viva Glam Lipstick, add to cart, verify checkout visible ---
def test_lip_search_add_to_cart_checkout(set_up_logged_in_browser):
    browser, page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.search("Lip")
    product = Product(page)
    product.click_viva_glam_lipstick()
    product.add_to_cart()
    cart = Cart(page)
    assert cart.checkout_visible()

# --- 5. Search nonsense, verify no results message ---
def test_search_no_product_message(set_up_logged_in_browser):
    browser, page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    nonsense = "dsadfsadsa"
    login.search(nonsense)
    cart = Cart(page)
    assert cart.search_no_results_visible()

# --- 6. Successful order ---
def test_successful_order_process(set_up_logged_in_browser):
    browser, page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.click_checkout_top_menu()
    cart = Cart(page)
    cart.wait_for_confirm_order()
    cart.confirm_order()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=15000)
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/success"

# --- 7. Empty cart flow (go to checkout, verify) ---
def test_empty_cart_checkout_result(set_up_logged_in_browser):
    browser, page = set_up_logged_in_browser
    page.goto("https://automationteststore.com/")
    login = LoginPage(page)
    login.click_checkout_top_menu()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=10000)
    cart = Cart(page)
    assert cart.is_empty_cart()