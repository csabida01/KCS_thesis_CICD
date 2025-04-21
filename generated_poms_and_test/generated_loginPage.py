class LoginPage:
    def __init__(self, page):
        self.page = page
        # Header
        self.login_or_register_selector = '.navbar-right #customer_menu_top li:nth-child(1) a'
        # Login Form
        self.login_name_selector = '#loginFrm_loginname'
        self.password_selector = '#loginFrm_password'
        self.login_button_selector = "button[title='Login']"
        self.login_error_selector = "div.alert.alert-error.alert-danger"
        # Search-bar
        self.search_bar_selector = "#filter_keyword"
        # Top menu (Checkout)
        self.menu_checkout_selector = "a.menu_checkout"

    def goto_login_page(self):
        self.page.wait_for_selector(self.login_or_register_selector, timeout=10000)
        self.page.click(self.login_or_register_selector)
        self.page.wait_for_selector(self.login_name_selector, timeout=10000)

    def login(self, username, password):
        self.page.fill(self.login_name_selector, username)
        self.page.fill(self.password_selector, password)
        self.page.wait_for_selector(self.login_button_selector, timeout=10000)
        self.page.click(self.login_button_selector)

    def search(self, keyword):
        self.page.wait_for_selector(self.search_bar_selector, timeout=10000)
        self.page.click(self.search_bar_selector)
        self.page.fill(self.search_bar_selector, keyword)
        self.page.keyboard.press('Enter')

    def click_checkout_top_menu(self):
        self.page.wait_for_selector(self.menu_checkout_selector, timeout=10000)
        self.page.click(self.menu_checkout_selector)

    def get_login_error(self):
        self.page.wait_for_selector(self.login_error_selector, timeout=10000)
        return self.page.inner_text(self.login_error_selector)

    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector, timeout=15000)
        return self.page.query_selector(selector)