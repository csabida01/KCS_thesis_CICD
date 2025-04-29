# generated_loginPage.py
from playwright.sync_api import Page, expect

class LoginPage:
    LOGIN_HEADER_LOGIN_OR_REGISTER = 'a[href="https://automationteststore.com/index.php?rt=account/login"]'
    USERNAME_INPUT = "#loginFrm_loginname"
    PASSWORD_INPUT = "#loginFrm_password"
    LOGIN_BUTTON = 'button.btn.btn-orange[title="Login"]'
    ERROR_MESSAGE = "div.alert.alert-error.alert-danger"
    SEARCH_BAR_INPUT = "#filter_keyword"
    TOP_MENU_CHECKOUT = "a.menu_checkout"

    def __init__(self, page: Page):
        self.page = page

    def click_login_header(self):
        self.page.wait_for_selector(self.LOGIN_HEADER_LOGIN_OR_REGISTER, timeout=10000)
        self.page.locator(self.LOGIN_HEADER_LOGIN_OR_REGISTER).click()

    def fill_username(self, username):
        self.page.wait_for_selector(self.USERNAME_INPUT, timeout=10000)
        self.page.fill(self.USERNAME_INPUT, username)

    def fill_password(self, password):
        self.page.wait_for_selector(self.PASSWORD_INPUT, timeout=10000)
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.page.wait_for_selector(self.LOGIN_BUTTON, timeout=10000)
        self.page.locator(self.LOGIN_BUTTON).click()

    def error_message_is_visible(self):
        return self.page.is_visible(self.ERROR_MESSAGE)

    def click_search_bar(self):
        self.page.wait_for_selector(self.SEARCH_BAR_INPUT, timeout=10000)
        self.page.locator(self.SEARCH_BAR_INPUT).click()

    def enter_keyword_and_press_enter(self, keyword):
        self.page.wait_for_selector(self.SEARCH_BAR_INPUT, timeout=10000)
        self.page.fill(self.SEARCH_BAR_INPUT, keyword)
        self.page.keyboard.press("Enter")

    def click_top_menu_checkout(self):
        self.page.wait_for_selector(self.TOP_MENU_CHECKOUT, timeout=10000)
        self.page.locator(self.TOP_MENU_CHECKOUT).click()