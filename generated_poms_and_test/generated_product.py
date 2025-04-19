class Product:
    def __init__(self, page):
        self.page = page

    # --- Product Search Page (grid) ---

    def get_search_grid_product_by_title(self, title):
        return self.page.locator(f'a.prdocutname[title="{title}"]')

    def get_search_grid_add_to_cart_by_product_id(self, product_id):
        # button is an <a class="productcart" data-id="...">
        return self.page.locator(f'a.productcart[data-id="{product_id}"]')

    # --- Product Details Page (datasheet) ---

    def get_datasheet_add_to_cart(self):
        # The only Add to Cart is <a class="cart"> with onclick containing 'form.submit()'
        return self.page.locator('ul.productpagecart a.cart')

    def get_colour_dropdown(self):
        return self.page.locator('select#option305')

    def get_quantity_input(self):
        return self.page.locator('input#product_quantity')

    def get_total_price_label(self):
        # Inside label, class 'total-price'
        return self.page.locator('span.total-price')

    # --- "There is no product..." message ---

    def get_no_product_message(self):
        return self.page.locator('div.contentpanel div:has-text("There is no product that matches the search criteria.")')