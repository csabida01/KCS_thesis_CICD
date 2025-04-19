class LoginPage:
    def __init__(self, page):
        self.page = page

    # Locators for header login link
    def login_or_register_link(self):
        return self.page.locator('a[href="https://automationteststore.com/index.php?rt=account/login"]:visible')
    
    # Locators for login box
    def loginname_input(self):
        return self.page.locator('input#loginFrm_loginname')

    def password_input(self):
        return self.page.locator('input#loginFrm_password')

    def login_button(self):
        return self.page.locator('button[title="Login"]')

    def login_error_message(self):
        return self.page.locator('div.alert.alert-error.alert-danger')

    # Account page proof element (for successful login)
    def account_dashboard(self):
        return self.page.locator('ul.side_account_list li.selected a[href="https://automationteststore.com/index.php?rt=account/account"]')

    # Top menu checkout (for cart test, visible after login)
    def top_checkout_link(self):
        return self.page.locator('a.menu_checkout')

    # Search bar from header
    def search_bar_input(self):
        return self.page.locator('input#filter_keyword')

    # Method for login
    def do_login(self, username, password):
        self.login_or_register_link().click()
        self.loginname_input().wait_for(state="visible", timeout=7000)
        self.loginname_input().fill(username)
        self.password_input().fill(password)
        self.login_button().click()