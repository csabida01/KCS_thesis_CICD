from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_homepage(self):
        self.page.goto("https://automationteststore.com/")
    
    def click_login_or_register(self):
        self.page.wait_for_selector('a[href="https://automationteststore.com/index.php?rt=account/login"]')
        self.page.locator('a[href="https://automationteststore.com/index.php?rt=account/login"]').first.click()

    def fill_username(self, username):
        self.page.wait_for_selector("#loginFrm_loginname")
        self.page.fill("#loginFrm_loginname", username)

    def fill_password(self, password):
        self.page.wait_for_selector("#loginFrm_password")
        self.page.fill("#loginFrm_password", password)

    def click_login_button(self):
        self.page.wait_for_selector('button[title="Login"]')
        self.page.locator('button[title="Login"]').click()

    def is_login_error(self):
        self.page.wait_for_selector('div.alert.alert-error.alert-danger', timeout=6000)
        return self.page.is_visible('div.alert.alert-error.alert-danger')

    def get_login_error_text(self):
        self.page.wait_for_selector('div.alert.alert-error.alert-danger')
        return self.page.locator('div.alert.alert-error.alert-danger').text_content()

    def is_logged_in(self):
        self.page.wait_for_selector('div.myaccountbox', timeout=10000)
        return self.page.is_visible('div.myaccountbox')

    def go_to_checkout_from_top_header(self):
        self.page.wait_for_selector('a.menu_checkout')
        self.page.locator('a.menu_checkout').first.click()