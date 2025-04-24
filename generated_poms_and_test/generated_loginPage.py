class LoginPage:
    def __init__(self, page):
        self.page = page

    # Header selectors
    LOGIN_OR_REGISTER_HEADER = "ul#customer_menu_top li a[href*='account/login']"
    LOGIN_MENU_TOPNAV = "ul#main_menu_top li[data-id='menu_account'] ul.sub_menu a.menu_login"

    # Login form
    USERNAME_INPUT = "input#loginFrm_loginname"
    PASSWORD_INPUT = "input#loginFrm_password"
    LOGIN_BUTTON = "button[title='Login']"

    # Error message
    LOGIN_ERROR_ALERT = "div.alert.alert-error.alert-danger"

    # My Account - for assertion after login
    MY_ACCOUNT_DASHBOARD_LINK = "ul.side_account_list li.selected a[href*='account/account']"

    def click_login_or_register(self):
        self.page.wait_for_selector(self.LOGIN_OR_REGISTER_HEADER)
        self.page.click(self.LOGIN_OR_REGISTER_HEADER)

    def click_login_from_dropdown(self):
        # This is for topnav menu
        self.page.hover("ul#main_menu_top li[data-id='menu_account']")
        self.page.wait_for_selector(self.LOGIN_MENU_TOPNAV)
        self.page.click(self.LOGIN_MENU_TOPNAV)

    def fill_username(self, username):
        self.page.wait_for_selector(self.USERNAME_INPUT)
        self.page.fill(self.USERNAME_INPUT, username)

    def fill_password(self, password):
        self.page.wait_for_selector(self.PASSWORD_INPUT)
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.page.wait_for_selector(self.LOGIN_BUTTON)
        self.page.click(self.LOGIN_BUTTON)

    def is_error_alert_visible(self):
        return self.page.is_visible(self.LOGIN_ERROR_ALERT)

    def is_account_dashboard_visible(self):
        return self.page.is_visible(self.MY_ACCOUNT_DASHBOARD_LINK)

    # For search bar in header (shared with product page flows)
    SEARCH_BAR_INPUT = "form#search_form input#filter_keyword"

    def search_for(self, search_term):
        self.page.wait_for_selector(self.SEARCH_BAR_INPUT)
        self.page.click(self.SEARCH_BAR_INPUT)
        self.page.fill(self.SEARCH_BAR_INPUT, search_term)
        self.page.keyboard.press('Enter')