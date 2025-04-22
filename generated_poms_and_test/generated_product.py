class Product:
    def __init__(self, page):
        self.page = page

    # PRODUCT GRID
    def click_product_by_title(self, product_title):
        locator = f'a[title="{product_title}"]'
        self.page.locator(locator).wait_for(state="visible", timeout=10000)
        self.page.locator(locator).click()

    def add_to_cart_from_grid_by_product_id(self, product_id):
        # <a data-id="59" ... class="productcart">
        locator = f'a.productcart[data-id="{product_id}"]'
        self.page.locator(locator).wait_for(state="visible", timeout=10000)
        self.page.locator(locator).click()

    # PRODUCT DETAILS PAGE
    def add_to_cart_from_details(self):
        # In Lipstick details page
        self.page.locator('ul.productpagecart li a.cart').wait_for(state="visible", timeout=10000)
        self.page.locator('ul.productpagecart li a.cart').click()

    # CART / CHECKOUT APPEARANCE AFTER ADD
    def is_checkout_button_appears(self):
        self.page.locator('a#cart_checkout1.btn.btn-orange[title="Checkout"]').wait_for(state="visible", timeout=10000)
        return self.page.is_visible('a#cart_checkout1.btn.btn-orange[title="Checkout"]')

    def get_no_results_text(self):
        self.page.locator('div.contentpanel > div').wait_for(state="visible", timeout=10000)
        return self.page.inner_text('div.contentpanel > div')

    # Lipstick: select a color (if needed)
    def select_color(self, color_option_text):
        self.page.locator('select#option305').wait_for(state="visible", timeout=10000)
        self.page.select_option('select#option305', label=color_option_text)

    def set_quantity(self, quantity):
        self.page.locator('input#product_quantity').wait_for(state="visible", timeout=10000)
        self.page.fill('input#product_quantity', str(quantity))