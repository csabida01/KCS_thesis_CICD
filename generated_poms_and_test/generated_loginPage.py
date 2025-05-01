class LoginPage:
    def __init__(self, page):
        self.page = page
        # Login/header
        self.login_or_register_link = "ul#customer_menu_top li a[href*='account/login']"
        self.search_input = "input#filter_keyword"
        self.search_bar_btn = "div.button-in-search"
        # Login box
        self.loginname_input = "input#loginFrm_loginname"
        self.password_input = "input#loginFrm_password"
        self.login_button = "button[title='Login']"
        self.login_error = "div.alert.alert-error.alert-danger"
        # Top Menu Checkout
        self.menu_checkout = "a.menu_checkout"
        # My account check
        self.my_account_dashboard_link = "ul.side_account_list li.selected a[href*='account/account']"

    def go_to_login(self):
        self.page.wait_for_selector(self.login_or_register_link)
        self.page.click(self.login_or_register_link)

    def login(self, username, password):
        self.page.wait_for_selector(self.loginname_input)
        self.page.fill(self.loginname_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_login_error(self):
        self.page.wait_for_selector(self.login_error, timeout=10000)
        return self.page.is_visible(self.login_error)

    def is_my_account_dashboard(self):
        self.page.wait_for_selector(self.my_account_dashboard_link, timeout=15000)
        return self.page.is_visible(self.my_account_dashboard_link)

    def search_for(self, keyword):
        # search input should be visible and ready
        self.page.wait_for_selector(self.search_input)
        self.page.fill(self.search_input, keyword)
        self.page.keyboard.press("Enter")

    def click_checkout_menu(self):
        self.page.wait_for_selector(self.menu_checkout)
        self.page.click(self.menu_checkout)