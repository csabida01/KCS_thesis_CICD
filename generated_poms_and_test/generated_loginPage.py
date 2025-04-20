class LoginPage:
    def __init__(self, page):
        self.page = page
        # From login header
        self.login_or_register_selector = '.navbar-right .block_2 #customernav #customer_menu_top li a[href*="account/login"]'
        # From login form
        self.username_selector = 'input#loginFrm_loginname'
        self.password_selector = 'input#loginFrm_password'
        self.login_button_selector = 'fieldset button.btn.btn-orange[title="Login"]'
        # Error
        self.error_selector = 'div.alert.alert-error.alert-danger'
        # From my account
        self.account_dashboard_selector = '.sidewidt .side_account_list li.selected a'
    
    def click_login_or_register(self):
        self.page.wait_for_selector(self.login_or_register_selector, timeout=15000)
        self.page.click(self.login_or_register_selector)

    def fill_username(self, username):
        self.page.wait_for_selector(self.username_selector, timeout=15000)
        self.page.fill(self.username_selector, username)

    def fill_password(self, password):
        self.page.wait_for_selector(self.password_selector, timeout=15000)
        self.page.fill(self.password_selector, password)

    def click_login_button(self):
        self.page.wait_for_selector(self.login_button_selector, timeout=15000)
        self.page.click(self.login_button_selector)

    def is_login_error_visible(self):
        try:
            self.page.wait_for_selector(self.error_selector, timeout=7000)
            return True
        except:
            return False

    def is_my_account_loaded(self):
        try:
            self.page.wait_for_selector(self.account_dashboard_selector, timeout=10000)
            return True
        except:
            return False