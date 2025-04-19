class Product:
    def __init__(self, page):
        self.page = page

    # Lipstick datasheet add to cart
    def datasheet_add_to_cart(self):
        return self.page.locator('ul.productpagecart a.cart')

    # On grid, add product by data-id (specific to search results)
    def grid_add_to_cart_viva_glam(self):
        return self.page.locator('a.productcart[data-id="59"]')

    def viva_glam_link_in_search_results(self):
        return self.page.locator('a[title="Viva Glam Lipstick"]').first

    # Lip search results
    def prdocutname_link(self, title):
        return self.page.locator(f'a.prdocutname[title="{title}"]').first

    # No product found message
    def no_results_found(self):
        return self.page.locator('div', has_text="There is no product that matches the search criteria.")

    # Search results grid
    def product_grid(self):
        return self.page.locator('div.thumbnails.grid.row.list-inline')