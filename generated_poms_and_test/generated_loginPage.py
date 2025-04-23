class LoginPage:
    def __init__(self, page):
        self.page = page
        # Header
        self.login_or_register_link = 'div#customernav ul#customer_menu_top a[href*="account/login"]'
        # Login form
        self.username_input = '#loginFrm_loginname'
        self.password_input = '#loginFrm_password'
        self.login_button = 'button[title="Login"]'
        self.login_error = 'div.alert.alert-error.alert-danger'
        # From 'my account' snippet, for successful login assertion
        self.account_dashboard_elem = 'ul.side_account_list li.selected a[href*="account/account"]'

    def goto_login(self):
        self.page.wait_for_selector(self.login_or_register_link, timeout=10000)
        self.page.click(self.login_or_register_link)

    def login(self, username, password):
        self.page.wait_for_selector(self.username_input, timeout=10000)
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.wait_for_selector(self.login_button, timeout=10000)
        self.page.click(self.login_button)

    def is_login_error_shown(self):
        try:
            self.page.wait_for_selector(self.login_error, timeout=5000)
            return True
        except:
            return False

    def is_logged_in(self):
        # Use selector uniquely present on "My Account" page
        try:
            self.page.wait_for_selector(self.account_dashboard_elem, timeout=10000)
            return True
        except:
            return False