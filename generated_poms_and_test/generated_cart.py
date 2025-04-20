class Cart:
    def __init__(self, page):
        self.page = page
        self.checkout_cart_top_selector = '.navbar-right .block_3 #topnav #main_menu_top a.menu_checkout'
        self.checkout_button_selector = 'a#cart_checkout1'
        self.update_button_selector = 'button#cart_update'
        self.cart_empty_header_selector = 'h1.heading1 .maintext .fa-frown'
        self.cart_empty_continue_button_selector = 'a.btn.btn-default[title="Continue"]'
        self.confirm_order_btn_selector = 'button#checkout_btn'

    def click_checkout_from_top(self):
        self.page.wait_for_selector(self.checkout_cart_top_selector, timeout=15000)
        self.page.click(self.checkout_cart_top_selector)
    
    def is_checkout_button_visible(self):
        try:
            self.page.wait_for_selector(self.checkout_button_selector, timeout=15000)
            return True
        except:
            return False

    def click_checkout_button(self):
        self.page.wait_for_selector(self.checkout_button_selector, timeout=15000)
        self.page.click(self.checkout_button_selector)

    def click_confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn_selector, timeout=25000)
        self.page.click(self.confirm_order_btn_selector)

    def is_cart_empty_header_visible(self):
        try:
            self.page.wait_for_selector(self.cart_empty_header_selector, timeout=12000)
            return True
        except:
            return False