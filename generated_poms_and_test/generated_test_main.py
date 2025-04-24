import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

# 1. Invalid login test
def test_login_with_invalid_credentials(set_up_fresh_browser):
    page = set_up_fresh_browser
    login = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login.click_login_or_register()
    login.fill_username("notexist")
    login.fill_password("wrongpassword")
    login.click_login_button()
    page.wait_for_timeout(1500)
    assert login.is_error_alert_visible()

# 2. Valid login test
def test_login_with_valid_credentials(set_up_fresh_browser):
    page = set_up_fresh_browser
    login = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login.click_login_or_register()
    login.fill_username("csaba.kelemen")
    login.fill_password("tesztteszt1")
    login.click_login_button()
    page.wait_for_timeout(1500)
    assert login.is_account_dashboard_visible()

# 3. Lipstick direct search and add to cart
def test_search_lipstick_and_add_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    product = Product(page)
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    login.search_for("Lipstick")
    # On product page, directly add to cart
    product.add_current_to_cart()
    page.wait_for_timeout(1500)
    # Should see the checkout button from the cart
    assert cart.is_checkout_button_visible()

# 4. Search for 'Lip', select from grid, add to cart
def test_search_lip_from_grid_and_add_viva_glam_lipstick(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    product = Product(page)
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    login.search_for("Lip")
    product.select_viva_glam_lipstick_from_search()
    product.add_current_to_cart()
    page.wait_for_timeout(1500)
    assert cart.is_checkout_button_visible()

# 5. No results for nonsense search
def test_search_for_nonsense_returns_no_results(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login = LoginPage(page)
    product = Product(page)
    page.goto("https://automationteststore.com/")
    login.search_for("dsadfsadsa")
    page.wait_for_timeout(1200)
    assert product.is_empty_results_alert_visible()

# 6. Successful checkout process
def test_complete_checkout_flow_success(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    cart.click_checkout_from_top_menu()
    cart.wait_for_confirm_order_button()
    cart.click_confirm_order_button()
    page.wait_for_timeout(1200)
    assert page.url.startswith("https://automationteststore.com/index.php?rt=checkout/success")

# 7. Empty cart scenario at checkout
def test_checkout_with_empty_cart_redirects_to_cart(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    cart.click_checkout_from_top_menu()
    page.wait_for_timeout(1000)
    assert page.url.startswith("https://automationteststore.com/index.php?rt=checkout/cart")