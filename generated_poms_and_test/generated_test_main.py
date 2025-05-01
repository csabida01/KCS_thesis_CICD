import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

# 1. Unsuccessful login
def test_invalid_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    login_page = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login_page.go_to_login()
    login_page.login("invalid_user", "wrong_password")
    assert login_page.get_login_error(), "Login error did not appear for wrong credentials"

# 2. Successful login
def test_successful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    login_page = LoginPage(page)
    page.goto("https://automationteststore.com/")
    login_page.go_to_login()
    login_page.login("csaba.kelemen", "tesztteszt1")
    assert login_page.is_my_account_dashboard(), "My Account dashboard not visible after successful login"

# 3. Search for "Lipstick" (single product, details-page flow) and check for checkout button after add to cart
def test_add_lipstick_from_detailsheet(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login_page = LoginPage(page)
    product = Product(page)
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    login_page.search_for("Lipstick")
    # There is no grid, single page, so just add to cart
    product.add_to_cart_on_detail()
    assert cart.can_see_checkout_btn(), "Checkout button is not visible after adding Lipstick to cart from detailsheet"

# 4. Search "Lip" (multi-product grid), click on Viva Glam Lipstick and add to cart, check checkout button
def test_add_lipstick_from_grid(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login_page = LoginPage(page)
    product = Product(page)
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    login_page.search_for("Lip")
    product.select_viva_glam_lipstick_from_grid()
    product.add_to_cart_on_detail()
    assert cart.can_see_checkout_btn(), "Checkout button is not visible after adding to cart from grid workflow"

# 5. Search for nonsense and check no product result
def test_search_no_results(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login_page = LoginPage(page)
    product = Product(page)
    page.goto("https://automationteststore.com/")
    login_page.search_for("dsadfsadsa")
    assert product.is_no_result_found(), "No product result message not found for nonsense search"

# 6. Checkout process, confirm order, check for processed order (success page url)
def test_checkout_confirm_success(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login_page = LoginPage(page)
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    login_page.click_checkout_menu()
    assert cart.wait_for_confirm_order(), "Confirm order button did not appear"
    cart.click_confirm_order()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=15000)
    assert page.url == "https://automationteststore.com/index.php?rt=checkout/success", "Did not navigate to success page after confirming order"

# 7. Enter cart from top menu and check for empty cart indicator
def test_checkout_cart_empty(set_up_logged_in_browser):
    page = set_up_logged_in_browser
    login_page = LoginPage(page)
    cart = Cart(page)
    page.goto("https://automationteststore.com/")
    login_page.click_checkout_menu()
    page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=15000)
    assert cart.cart_is_empty(), "Empty cart indicator not found after going to cart"