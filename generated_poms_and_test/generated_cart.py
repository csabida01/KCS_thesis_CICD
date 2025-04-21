class Cart:
    def __init__(self, page):
        self.page = page
        # Checkout button in cart
        self.checkout_btn_selector = "#cart_checkout1"
        # Confirm Order
        self.confirm_order_btn_selector = "#checkout_btn"
        # Empty cart message
        self.empty_cart_message_selector = "h1.heading1 .maintext i.fa-frown"
        # Order Success: 
        self.order_success_heading_selector = "h1.heading1 .maintext i.fa-thumbs-up"
        self.no_results_message_selector = "div.contentpanel div:has-text('There is no product that matches the search criteria.')"
        # My Account: take "Edit account details"
        self.account_edit_details_selector = "a[href*='account/edit']"

    def checkout_visible(self):
        self.page.wait_for_selector(self.checkout_btn_selector, timeout=10000)
        return self.page.is_visible(self.checkout_btn_selector)

    def proceed_checkout(self):
        self.page.wait_for_selector(self.checkout_btn_selector, timeout=10000)
        self.page.click(self.checkout_btn_selector)

    def wait_for_confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn_selector, timeout=10000)

    def confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn_selector, timeout=10000)
        self.page.click(self.confirm_order_btn_selector)

    def is_order_success(self):
        self.page.wait_for_selector(self.order_success_heading_selector, timeout=10000)
        return self.page.is_visible(self.order_success_heading_selector)

    def is_empty_cart(self):
        self.page.wait_for_selector("h1.heading1 .maintext", timeout=10000)
        text = self.page.inner_text("h1.heading1 .maintext")
        return "Shopping Cart" in text

    def search_no_results_visible(self):
        self.page.wait_for_selector("div.contentpanel", timeout=10000)
        text = self.page.inner_text("div.contentpanel")
        return "There is no product that matches the search criteria." in text

    def account_edit_details_visible(self):
        self.page.wait_for_selector(self.account_edit_details_selector, timeout=10000)
        return self.page.is_visible(self.account_edit_details_selector)