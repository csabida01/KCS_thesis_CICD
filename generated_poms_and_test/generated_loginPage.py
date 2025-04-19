class LoginPage:
    def __init__(self, page):
        self.page = page

    # Header selectors
    def login_or_register_link(self):
        return self.page.locator('a[href="https://automationteststore.com/index.php?rt=account/login"]', has_text="Login or register").first

    def search_bar_input(self):
        return self.page.locator('input#filter_keyword')

    def top_checkout(self):
        return self.page.locator('a.menu_checkout').first

    # Login form selectors
    def username_input(self):
        return self.page.locator('input#loginFrm_loginname')

    def password_input(self):
        return self.page.locator('input#loginFrm_password')

    def login_button(self):
        return self.page.locator('button[title="Login"]')

    def error_message(self):
        return self.page.locator('div.alert.alert-error.alert-danger')

    # My Account confirmation element
    def my_account_h2(self):
        return self.page.locator('h2.heading2', has_text="My Account")