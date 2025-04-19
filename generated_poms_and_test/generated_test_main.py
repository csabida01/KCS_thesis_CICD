import time
import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

@pytest.mark.usefixtures("set_up_fresh_browser", "set_up_logged_in_browser")
class TestAutomationTestStore:

    # 1. Invalid login test
    def test_invalid_login(self, set_up_fresh_browser):
        page = set_up_fresh_browser
        login = LoginPage(page)
        page.goto("https://automationteststore.com/")
        login.login_or_register_link().wait_for(state="visible", timeout=10000)
        login.login_or_register_link().click()
        login.username_input().wait_for(state="visible", timeout=10000)
        login.username_input().fill("invalid_user")
        login.password_input().fill("invalid_pass")
        login.login_button().wait_for(state="attached", timeout=10000)
        login.login_button().click()
        login.error_message().wait_for(state="visible", timeout=10000)
        assert login.error_message().is_visible()

    # 2. Valid login and account access test
    def test_valid_login_and_account(self, set_up_fresh_browser):
        page = set_up_fresh_browser
        login = LoginPage(page)
        page.goto("https://automationteststore.com/")
        login.login_or_register_link().wait_for(state="visible", timeout=10000)
        login.login_or_register_link().click()
        login.username_input().wait_for(state="visible", timeout=10000)
        login.username_input().fill("csaba.kelemen")
        login.password_input().fill("tesztteszt1")
        login.login_button().wait_for(state="attached", timeout=10000)
        login.login_button().click()
        login.my_account_h2().wait_for(state="visible", timeout=10000)
        assert login.my_account_h2().is_visible()

    # 3. Search and add to cart (single product page) & checkout
    def test_lipstick_search_and_add_to_cart(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login = LoginPage(page)
        product = Product(page)
        cart = Cart(page)

        page.goto("https://automationteststore.com/")
        login.search_bar_input().wait_for(state="visible", timeout=10000)
        login.search_bar_input().click()
        login.search_bar_input().fill("Lipstick")
        login.search_bar_input().press("Enter")
        # Assume redirected directly to product page with input "Lipstick"
        product.datasheet_add_to_cart().wait_for(state="visible", timeout=10000)
        product.datasheet_add_to_cart().click()
        cart.checkout_button().wait_for(state="visible", timeout=10000)
        assert cart.checkout_button().is_visible()

    # 4. Search grid, select Viva Glam, add to cart, then checkout
    def test_lip_search_grid_add_to_cart(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login = LoginPage(page)
        product = Product(page)
        cart = Cart(page)

        page.goto("https://automationteststore.com/")
        login.search_bar_input().wait_for(state="visible", timeout=10000)
        login.search_bar_input().click()
        login.search_bar_input().fill("Lip")
        login.search_bar_input().press("Enter")
        product.viva_glam_link_in_search_results().wait_for(state="visible", timeout=15000)
        product.viva_glam_link_in_search_results().click()
        product.datasheet_add_to_cart().wait_for(state="visible", timeout=10000)
        product.datasheet_add_to_cart().click()
        cart.checkout_button().wait_for(state="visible", timeout=10000)
        assert cart.checkout_button().is_visible()

    # 5. Search nonsense and check no result appears
    def test_nonsense_search_finds_no_product(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login = LoginPage(page)
        product = Product(page)

        page.goto("https://automationteststore.com/")
        login.search_bar_input().wait_for(state="visible", timeout=10000)
        login.search_bar_input().click()
        login.search_bar_input().fill("dsadfsadsa")
        login.search_bar_input().press("Enter")
        product.no_results_found().wait_for(state="visible", timeout=10000)
        assert product.no_results_found().is_visible()

    # 6. Checkout flow and order confirmation
    def test_checkout_and_confirm_order(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login = LoginPage(page)
        cart = Cart(page)

        page.goto("https://automationteststore.com/")
        login.top_checkout().wait_for(state="visible", timeout=10000)
        login.top_checkout().click()
        cart.confirm_order_btn().wait_for(state="visible", timeout=20000)
        cart.confirm_order_btn().click()
        page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=20000)
        assert "checkout/success" in page.url

    # 7. Checkout on empty cart
    def test_checkout_empty_cart(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login = LoginPage(page)

        page.goto("https://automationteststore.com/")
        login.top_checkout().wait_for(state="visible", timeout=10000)
        login.top_checkout().click()
        page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart", timeout=10000)
        assert "checkout/cart" in page.url