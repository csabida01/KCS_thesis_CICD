import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart
from playwright.sync_api import expect

@pytest.mark.usefixtures("set_up_fresh_browser")
class TestLogin:
    def test_invalid_login(self, set_up_fresh_browser):
        page = set_up_fresh_browser
        page.goto("https://automationteststore.com/")
        login = LoginPage(page)

        # Click Login or register
        login_link = login.get_login_or_register_link()
        login_link.wait_for(state='visible', timeout=8000)
        login_link.click()

        # On the login form
        login.get_login_name_input().wait_for(state='visible', timeout=8000)
        login.get_login_name_input().fill("invaliduser")
        login.get_password_input().fill("wrongpass")
        login.get_login_button().click()

        # Wait for error
        err = login.get_login_error()
        err.wait_for(state='visible', timeout=8000)
        assert "Incorrect login" in err.inner_text()

    def test_valid_login(self, set_up_fresh_browser):
        page = set_up_fresh_browser
        page.goto("https://automationteststore.com/")
        login = LoginPage(page)

        # Click Login or register
        login_link = login.get_login_or_register_link()
        login_link.wait_for(state='visible', timeout=8000)
        login_link.click()

        # On login form
        login.get_login_name_input().wait_for(state='visible', timeout=8000)
        login.get_login_name_input().fill("csaba.kelemen")
        login.get_password_input().fill("tesztteszt1")
        login.get_login_button().click()

        # After login, check for "Account Dashboard" element (My Account box)
        acc_link = login.get_my_account_dashboard_link()
        acc_link.wait_for(state='visible', timeout=8000)
        assert acc_link.is_visible()