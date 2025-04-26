class LoginPage:
    def __init__(self, page):
        self.page = page

    # HEADER
    def goto_login(self):
        self.page.wait_for_selector('.navbar-right .block_2 #customernav #customer_menu_top > li > a')
        self.page.click('.navbar-right .block_2 #customernav #customer_menu_top > li > a')

    # LOGIN BOX
    def login(self, username, password):
        self.page.wait_for_selector('#loginFrm_loginname')
        self.page.fill('#loginFrm_loginname', username)
        self.page.fill('#loginFrm_password', password)
        self.page.wait_for_selector('button.btn-orange[title="Login"]')
        self.page.click('button.btn-orange[title="Login"]')

    def get_login_error(self):
        self.page.wait_for_selector('div.alert.alert-error.alert-danger')
        return self.page.inner_text('div.alert.alert-error.alert-danger')

    # MY ACCOUNT PAGE
    def is_on_my_account(self):
        self.page.wait_for_selector('div.myaccountbox ul.side_account_list li.selected a')
        return self.page.is_visible('div.myaccountbox ul.side_account_list li.selected a')