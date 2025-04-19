class Product:
    def __init__(self, page):
        self.page = page
        # search-bar input in header
        self.search_input = '#filter_keyword'
        # search result grid (Lip search)
        self.viva_glam_lipstick_title = 'a[title="Viva Glam Lipstick"]'
        # Lipstick datasheet product add to cart
        self.add_to_cart_link = '.productpagecart li a.cart'
        # Add to cart in grid
        self.grid_add_to_cart_button = 'a.productcart[data-id="59"]'
        # Indicator for no results
        self.no_result_message = 'div.contentpanel > div:has-text("There is no product that matches the search criteria.")'

    def search_product(self, keyword):
        self.page.wait_for_selector(self.search_input, timeout=10000)
        self.page.fill(self.search_input, keyword)
        self.page.keyboard.press('Enter')

    def click_add_to_cart_datasheet(self):
        self.page.wait_for_selector(self.add_to_cart_link, timeout=10000)
        self.page.click(self.add_to_cart_link)

    def click_result_by_title(self, title="Viva Glam Lipstick"):
        self.page.wait_for_selector(f'a[title="{title}"]', timeout=10000)
        self.page.click(f'a[title="{title}"]')

    def click_add_to_cart_grid(self, product_id="59"):
        self.page.wait_for_selector(f'a.productcart[data-id="{product_id}"]', timeout=10000)
        self.page.click(f'a.productcart[data-id="{product_id}"]')

    def is_no_results_message_visible(self):
        self.page.wait_for_selector(self.no_result_message, timeout=10000)
        return self.page.is_visible(self.no_result_message)