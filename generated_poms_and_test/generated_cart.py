class Cart:
    # Checkout and confirmation selectors
    CHECKOUT_BUTTON = 'a#cart_checkout1'
    CONFIRM_ORDER_BUTTON = 'button#checkout_btn'
    CART_UPDATE_BUTTON = 'button#cart_update'
    EMPTY_CART_HEADER = 'h1.heading1 span.maintext:has-text("Shopping Cart")'
    EMPTY_CART_MESSAGE = 'div.contentpanel:has-text("Your shopping cart is empty!")'

    @staticmethod
    def can_see_checkout(page):
        page.wait_for_selector(Cart.CHECKOUT_BUTTON, timeout=15000)
        return page.is_visible(Cart.CHECKOUT_BUTTON)

    @staticmethod
    def do_checkout(page):
        page.wait_for_selector(Cart.CHECKOUT_BUTTON, timeout=15000)
        page.click(Cart.CHECKOUT_BUTTON)

    @staticmethod
    def do_confirm_order(page):
        page.wait_for_selector(Cart.CONFIRM_ORDER_BUTTON, timeout=15000)
        page.click(Cart.CONFIRM_ORDER_BUTTON)

    @staticmethod
    def is_order_success(page):
        # Check for URL and order processed header
        page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=20000)
        selector = 'h1.heading1 span.maintext:has-text("Your Order Has Been Processed!")'
        return page.is_visible(selector)

    @staticmethod
    def is_cart_empty(page):
        # Check if main header and message are visible
        page.wait_for_selector(Cart.EMPTY_CART_HEADER, timeout=15000)
        page.wait_for_selector(Cart.EMPTY_CART_MESSAGE, timeout=15000)
        return page.is_visible(Cart.EMPTY_CART_HEADER) and page.is_visible(Cart.EMPTY_CART_MESSAGE)