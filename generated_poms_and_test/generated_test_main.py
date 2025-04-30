import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart

AUTOMATIONTESTSTORE = "https://automationteststore.com/"

@pytest.mark.usefixtures('set_up_fresh_browser')
def test_unsuccessful_login(set_up_fresh_browser):
    page = set_up_fresh_browser
    page.goto(AUTOMATIONTESTSTORE)
    login_page = LoginPage(page)
    login_page.goto_login()
    login_page.fill_login_name("invaliduser")
    login_page.fill_password("invalidpass")
    login_page.click_login()
    assert "Incorrect login or password provided" in login_page.get_login_error()