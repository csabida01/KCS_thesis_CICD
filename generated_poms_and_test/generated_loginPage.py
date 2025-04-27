class LoginPage:
    URL = "https://automationteststore.com/index.php?rt=account/login"

    # CSS Selectors from the login page HTML snippet
    LOGIN_LINK_HEADER = 'a[href="https://automationteststore.com/index.php?rt=account/login"]'
    USERNAME_INPUT = '#loginFrm_loginname'
    PASSWORD_INPUT = '#loginFrm_password'
    LOGIN_BUTTON = 'button[title="Login"]'
    ERROR_ALERT = 'div.alert.alert-error.alert-danger'

    def __init__(self, page):
        self.page = page

    def goto_login(self):
        self.page.wait_for_selector(self.LOGIN_LINK_HEADER, timeout=15000)
        self.page.click(self.LOGIN_LINK_HEADER)
        self.page.wait_for_selector(self.USERNAME_INPUT, timeout=15000)

    def login(self, username, password):
        self.page.wait_for_selector(self.USERNAME_INPUT, timeout=15000)
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.wait_for_selector(self.LOGIN_BUTTON, timeout=15000)
        self.page.click(self.LOGIN_BUTTON)

    def check_login_error(self):
        self.page.wait_for_selector(self.ERROR_ALERT, timeout=15000)
        return self.page.is_visible(self.ERROR_ALERT)

    def fill_search_and_submit(self, text):
        self.page.wait_for_selector('input#filter_keyword', timeout=15000)
        self.page.fill('input#filter_keyword', text)
        self.page.press('input#filter_keyword', 'Enter')

    def click_checkout_header(self):
        self.page.wait_for_selector('a.menu_checkout', timeout=15000)
        self.page.click('a.menu_checkout')