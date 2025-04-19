class LoginPage:
    def __init__(self, page):
        self.page = page
        # header selectors
        self.login_or_register_link = 'a[href="https://automationteststore.com/index.php?rt=account/login"]'
        self.menu_login_link = 'li[data-id="menu_login"] a.menu_login'
        # login page selectors
        self.login_username_input = 'input#loginFrm_loginname'
        self.login_password_input = 'input#loginFrm_password'
        self.login_button = 'button[title="Login"]'
        self.error_message = 'div.alert.alert-error.alert-danger'
        # account selectors
        self.account_dashboard = 'ul.side_account_list li.selected a[href*="account/account"]'

    def goto_login(self):
        self.page.wait_for_selector(self.login_or_register_link, timeout=10000)
        self.page.click(self.login_or_register_link)

    def do_login(self, username, password):
        self.page.wait_for_selector(self.login_username_input, timeout=10000)
        self.page.fill(self.login_username_input, username)
        self.page.fill(self.login_password_input, password)
        self.page.click(self.login_button)

    def is_error_message_visible(self):
        return self.page.is_visible(self.error_message)

    def is_account_dashboard_visible(self):
        return self.page.is_visible(self.account_dashboard)