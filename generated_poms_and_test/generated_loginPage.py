class LoginPage:
    def __init__(self, page):
        self.page = page

    # HEADER NAV
    def login_or_register(self):
        # "Login or register" link in top header
        self.page.locator('a[href="https://automationteststore.com/index.php?rt=account/login"]').first.wait_for(state="visible", timeout=10000)
        self.page.locator('a[href="https://automationteststore.com/index.php?rt=account/login"]').first.click()

    # LOGIN FORM
    def fill_login_name(self, username):
        self.page.locator('input#loginFrm_loginname').wait_for(state="visible", timeout=10000)
        self.page.fill('input#loginFrm_loginname', username)

    def fill_password(self, password):
        self.page.locator('input#loginFrm_password').wait_for(state="visible", timeout=10000)
        self.page.fill('input#loginFrm_password', password)

    def submit(self):
        self.page.locator('button.btn.btn-orange[title="Login"]').wait_for(state="visible", timeout=10000)
        self.page.locator('button.btn.btn-orange[title="Login"]').click()

    # ERROR / ALERT
    def get_login_error(self):
        # Wait until the error box is visible (if any)
        self.page.locator('div.alert.alert-error.alert-danger').wait_for(state="visible", timeout=10000)
        return self.page.inner_text('div.alert.alert-error.alert-danger')

    # SEARCH
    def search_for(self, search_text):
        self.page.locator('input#filter_keyword').wait_for(state="visible", timeout=10000)
        self.page.fill('input#filter_keyword', search_text)
        self.page.keyboard.press("Enter")

    def click_checkout_top_menu(self):
        self.page.locator('a.menu_checkout').first.wait_for(state="visible", timeout=10000)
        self.page.locator('a.menu_checkout').first.click()