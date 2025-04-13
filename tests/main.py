from POMs.loginPage import LoginPage
from POMs.product import Product
from POMs.cart import Cart


def test_successful_login(set_up_fresh_browser):
    login_page = LoginPage(set_up_fresh_browser)
    login_page.login("csaba.kelemen", "tesztteszt1")
    assert login_page.is_logged_in() == True


def test_unsuccessful_login(set_up_fresh_browser):
    login_page = LoginPage(set_up_fresh_browser)
    login_page.login("rossz_user", "asdasd")
    assert login_page.is_logged_in() == False


def test_search_for_one_result(set_up_logged_in_browser):
    product = Product(set_up_logged_in_browser)
    product.product_search("lipstick")
    product.add_product_to_cart()
    assert product.is_product_added() == True


def test_search_for_more_results(set_up_logged_in_browser):
    product = Product(set_up_logged_in_browser)
    product.product_search("pour")
    product.add_product_to_cart()
    assert product.is_product_added() == True


def test_search_for_zero_result(set_up_logged_in_browser):
    product = Product(set_up_logged_in_browser)
    product.product_search("Random product")
    product.add_product_to_cart()
    assert product.is_product_added() == False


def test_checkout(set_up_logged_in_browser):
    cart = Cart(set_up_logged_in_browser)
    cart.view_cart_content()
    cart.buy_products()
    assert cart.is_purchase_successful() == True


def test_cart_empty(set_up_logged_in_browser):
    cart = Cart(set_up_logged_in_browser)
    cart.view_cart_content()
    assert cart.is_cart_empty() == True