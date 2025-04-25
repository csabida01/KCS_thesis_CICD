class LoginPage:
    def __init__(self, page):
        self.page = page

    # Header login/register
    def click_login_or_register(self):
        self.page.wait_for_selector('a[href="https://automationteststore.com/index.php?rt=account/login"]', timeout=10000)
        self.page.click('a[href="https://automationteststore.com/index.php?rt=account/login"]')

    # Username, password
    def fill_login_name(self, username):
        self.page.wait_for_selector('#loginFrm_loginname', timeout=10000)
        self.page.fill('#loginFrm_loginname', username)

    def fill_password(self, password):
        self.page.wait_for_selector('#loginFrm_password', timeout=10000)
        self.page.fill('#loginFrm_password', password)

    # Login button
    def click_login_button(self):
        self.page.wait_for_selector('button[title="Login"]', timeout=10000)
        self.page.click('button[title="Login"]')

    # Login error
    def is_login_error_visible(self):
        return self.page.is_visible('div.alert.alert-error.alert-danger')

    # Check My Account any element (e.g. Logoff link)
    def is_my_account_visible(self):
        return self.page.is_visible('a[href="https://automationteststore.com/index.php?rt=account/logout"]')