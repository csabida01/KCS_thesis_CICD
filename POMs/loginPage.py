import os
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://automationteststore.com/")
        self.login_menu_button = page.get_by_role("link", name="Login or register")
        self.username_input = page.locator("#loginFrm_loginname")
        self.password_input = page.locator("#loginFrm_password")
        self.login_button = page.get_by_role("button", name="Login")
        self.my_account = page.get_by_text("My Account").first

    def login(self, username, password):
        self.login_menu_button.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_logged_in(self):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        json_path = os.path.join(project_root, "logged_in_state.json")
        if self.my_account.is_visible():
            self.page.context.storage_state(path=json_path)
        return self.my_account.is_visible()
