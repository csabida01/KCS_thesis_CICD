class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_or_register_link = 'a[href="https://automationteststore.com/index.php?rt=account/login"]'
        self.login_name_input = '#loginFrm_loginname'
        self.password_input = '#loginFrm_password'
        self.login_button = 'button.btn.btn-orange.pull-right[title="Login"]'
        self.login_error = 'div.alert.alert-error.alert-danger'

    def goto_login(self):
        self.page.wait_for_selector(self.login_or_register_link)
        self.page.click(self.login_or_register_link)

    def fill_login_name(self, username):
        self.page.wait_for_selector(self.login_name_input)
        self.page.fill(self.login_name_input, username)

    def fill_password(self, password):
        self.page.wait_for_selector(self.password_input)
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.wait_for_selector(self.login_button)
        self.page.click(self.login_button)

    def get_login_error(self):
        self.page.wait_for_selector(self.login_error)
        return self.page.inner_text(self.login_error)

    def login(self, username, password):
        self.goto_login()
        self.fill_login_name(username)
        self.fill_password(password)
        self.click_login()