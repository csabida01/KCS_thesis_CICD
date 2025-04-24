class Cart:
    def __init__(self, page):
        self.page = page

    # Checkout button in cart page
    CHECKOUT_BUTTON = "a#cart_checkout1"
    CONFIRM_ORDER_BUTTON = "button#checkout_btn"
    EMPTY_CART_ALERT = "h1.heading1 span.maintext:has-text('Shopping Cart')"
    MAIN_MENU_CHECKOUT_LINK = "ul#main_menu_top a.menu_checkout"

    def click_checkout_from_top_menu(self):
        self.page.wait_for_selector(self.MAIN_MENU_CHECKOUT_LINK)
        self.page.click(self.MAIN_MENU_CHECKOUT_LINK)

    def click_checkout_button(self):
        self.page.wait_for_selector(self.CHECKOUT_BUTTON)
        self.page.click(self.CHECKOUT_BUTTON)

    def wait_for_confirm_order_button(self):
        self.page.wait_for_selector(self.CONFIRM_ORDER_BUTTON)

    def click_confirm_order_button(self):
        self.page.wait_for_selector(self.CONFIRM_ORDER_BUTTON)
        self.page.click(self.CONFIRM_ORDER_BUTTON)

    def is_checkout_button_visible(self):
        return self.page.is_visible(self.CHECKOUT_BUTTON)

    def is_empty_cart_visible(self):
        self.page.wait_for_selector(self.EMPTY_CART_ALERT)
        return self.page.is_visible(self.EMPTY_CART_ALERT)