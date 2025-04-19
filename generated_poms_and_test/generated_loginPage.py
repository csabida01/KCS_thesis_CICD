class LoginPage:
    def __init__(self, page):
        self.page = page

    # Header elements
    def get_login_or_register_link(self):
        return self.page.locator('ul#customer_menu_top a[href*="account/login"]')

    def get_search_bar_input(self):
        return self.page.locator('input#filter_keyword')

    def get_top_menu_checkout(self):
        return self.page.locator('a.menu_checkout')

    # Login form elements
    def get_login_name_input(self):
        return self.page.locator('input#loginFrm_loginname')

    def get_password_input(self):
        return self.page.locator('input#loginFrm_password')

    def get_login_button(self):
        # There may be multiple buttons with title='Login', but this is under fieldset in the login box
        return self.page.locator('fieldset button[title="Login"]')

    def get_login_error(self):
        return self.page.locator('div.alert.alert-error.alert-danger')

    # Detect "My Account" (on the account dashboard)
    def get_my_account_dashboard_link(self):
        # Find by side_account_list > selected element
        return self.page.locator('ul.side_account_list li.selected a[href*="account/account"]')