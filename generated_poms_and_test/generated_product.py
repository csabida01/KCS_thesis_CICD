class Product:
    def __init__(self, page):
        self.page = page

    # For product search results grid: select "Viva Glam Lipstick"
    def viva_glam_lipstick_link(self):
        return self.page.locator('a[title="Viva Glam Lipstick"]')

    # Lipstick product page
    def color_dropdown(self):
        return self.page.locator('select#option305')

    def quantity_box(self):
        return self.page.locator('input#product_quantity')

    # Add to cart button (only one in product data sheet)
    def add_to_cart_data_sheet(self):
        return self.page.locator('ul.productpagecart a.cart')

    # In grid results (search Lip): Add to cart for each product (take for Viva Glam)
    def viva_glam_grid_add_to_cart(self):
        # the "Add to cart" for Viva Glam Lipstick product_id=59 in search grid
        return self.page.locator('a[data-id="59"].productcart')

    # Result 'no product'
    def no_product_found_msg(self):
        return self.page.locator('div:has-text("There is no product that matches the search criteria.")')

    # Fill search box in the header
    def fill_search_bar(self, keyword):
        bar = self.page.locator('input#filter_keyword')
        bar.click()
        bar.fill(keyword)
        bar.press('Enter')