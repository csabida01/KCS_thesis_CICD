class Product:
    def __init__(self, page):
        self.page = page
        # For grid result - Viva Glam Lipstick link
        self.viva_glam_lipstick_link = 'a[title="Viva Glam Lipstick"]'
        # Add to cart on grid result, for specific product via data-id attr or correct href (for product_id=59)
        self.add_to_cart_grid_viva_glam = "a[data-id='59'].productcart"
        # Add to cart on product sheet
        self.add_to_cart_on_detailsheet = "ul.productpagecart li a.cart"
        # For product quantity on detailsheet
        self.quantity_input = "input#product_quantity"
        # For color/option select, not used for now, could be handled if required
        self.color_select = "select#option305"
        # No result found locator
        self.no_product_div = "div.contentpanel > div:has-text('There is no product that matches the search criteria.')"

    def select_viva_glam_lipstick_from_grid(self):
        self.page.wait_for_selector(self.viva_glam_lipstick_link, timeout=15000)
        self.page.click(self.viva_glam_lipstick_link)

    def add_to_cart_from_grid(self):
        self.page.wait_for_selector(self.add_to_cart_grid_viva_glam, timeout=12000)
        self.page.click(self.add_to_cart_grid_viva_glam)

    def add_to_cart_on_detail(self):
        self.page.wait_for_selector(self.add_to_cart_on_detailsheet, timeout=12000)
        self.page.click(self.add_to_cart_on_detailsheet)

    def is_no_result_found(self):
        self.page.wait_for_selector(self.no_product_div, timeout=8000)
        return self.page.is_visible(self.no_product_div)