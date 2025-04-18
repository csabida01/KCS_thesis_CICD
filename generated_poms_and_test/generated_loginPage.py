class LoginPage:
    LOGIN_OR_REGISTER_SELECTOR = 'a[href="https://automationteststore.com/index.php?rt=account/login"]'
    USERNAME_INPUT_SELECTOR = 'input#loginFrm_loginname'
    PASSWORD_INPUT_SELECTOR = 'input#loginFrm_password'
    LOGIN_BUTTON_SELECTOR = 'button[title="Login"]'
    LOGIN_ERROR_SELECTOR = 'div.alert.alert-error.alert-danger'

    def __init__(self, page):
        self.page = page

    def click_login_or_register(self):
        self.page.wait_for_selector(self.LOGIN_OR_REGISTER_SELECTOR, timeout=15000)
        self.page.click(self.LOGIN_OR_REGISTER_SELECTOR)

    def fill_username(self, username):
        self.page.wait_for_selector(self.USERNAME_INPUT_SELECTOR, timeout=15000)
        self.page.fill(self.USERNAME_INPUT_SELECTOR, username)

    def fill_password(self, password):
        self.page.wait_for_selector(self.PASSWORD_INPUT_SELECTOR, timeout=15000)
        self.page.fill(self.PASSWORD_INPUT_SELECTOR, password)

    def click_login_button(self):
        self.page.wait_for_selector(self.LOGIN_BUTTON_SELECTOR, timeout=15000)
        self.page.click(self.LOGIN_BUTTON_SELECTOR)

    def is_error_message_visible(self):
        try:
            self.page.wait_for_selector(self.LOGIN_ERROR_SELECTOR, timeout=10000)
            return True
        except Exception:
            return False