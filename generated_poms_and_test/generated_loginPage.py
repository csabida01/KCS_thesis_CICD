class LoginPage:
    URL = "https://automationteststore.com/index.php?rt=account/login"

    def __init__(self, page):
        self.page = page

    @property
    def login_username_input(self):
        return self.page.locator('input#loginFrm_loginname')

    @property
    def login_password_input(self):
        return self.page.locator('input#loginFrm_password')

    @property
    def login_button(self):
        return self.page.locator('button.btn.btn-orange[title="Login"]')

    @property
    def login_error_message(self):
        return self.page.locator('div.alert.alert-error.alert-danger')

    def login(self, username, password):
        self.login_username_input.wait_for(state='visible')
        self.login_username_input.fill(username)
        self.login_password_input.fill(password)
        self.login_button.wait_for(state='visible')
        self.login_button.click()

    def get_login_error_message(self):
        self.login_error_message.wait_for(state='visible')
        return self.login_error_message.inner_text().strip()

    def on_page(self):
        return self.page.url.startswith(self.URL)