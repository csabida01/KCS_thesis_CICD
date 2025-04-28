import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

@pytest.mark.usefixtures("set_up_fresh_browser")
class TestLogin:
    def test_unsuccessful_login(self, set_up_fresh_browser):
        page = set_up_fresh_browser
        login_page = LoginPage(page)
        login_page.goto_homepage()
        login_page.click_login_or_register()
        login_page.fill_username("invalid_user")
        login_page.fill_password("invalid_pass")
        login_page.click_login_button()
        assert login_page.is_login_error()
        error_text = login_page.get_login_error_text()
        assert "Incorrect login or password" in error_text

    def test_successful_login(self, set_up_fresh_browser):
        page = set_up_fresh_browser
        login_page = LoginPage(page)
        login_page.goto_homepage()
        login_page.click_login_or_register()
        login_page.fill_username("csaba.kelemen")
        login_page.fill_password("tesztteszt1")
        login_page.click_login_button()
        assert login_page.is_logged_in()
        # try to get element from Update and checkout (the checkout button)
        cart = Cart(page)
        assert cart.is_checkout_visible()

@pytest.mark.usefixtures("set_up_logged_in_browser")
class TestProductAndCart:
    def test_direct_product_add_to_cart(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        product = Product(page)
        cart = Cart(page)
        # search for 'Lipstick' (brings you to the datasheet)
        product.search_for_product("Lipstick")
        # no grid, direct datasheet add to cart possible
        product.add_current_product_to_cart()
        # should land on cart
        assert cart.is_checkout_visible()

    def test_flow_grid_lip_add_viva_glam_lipstick(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        product = Product(page)
        cart = Cart(page)
        product.search_for_product("Lip")
        # select Viva Glam Lipstick grid result
        product.click_result_by_title("Viva Glam Lipstick")
        # add to cart on datasheet
        product.add_current_product_to_cart()
        assert cart.is_checkout_visible()

    def test_search_nonsense_no_product(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        product = Product(page)
        product.search_for_product("dsadfsadsa")
        assert product.is_no_search_results_message_visible()

    def test_checkout_full_cart_confirm_order(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login_page = LoginPage(page)
        cart = Cart(page)
        # click checkout from top header
        login_page.go_to_checkout_from_top_header()
        # click confirm order when visible
        cart.click_confirm_order()
        # check URL for success
        page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success")
        assert "success" in page.url
        # additional check for order processed message
        assert cart.order_success_message_visible()

    def test_checkout_empty_cart(self, set_up_logged_in_browser):
        page = set_up_logged_in_browser
        login_page = LoginPage(page)
        cart = Cart(page)
        # click checkout from top header
        login_page.go_to_checkout_from_top_header()
        # should redirect to the cart, so get url and check if empty
        page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/cart")
        assert "cart" in page.url
        assert cart.is_cart_empty()