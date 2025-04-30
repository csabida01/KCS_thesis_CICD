class Product:
    def __init__(self, page):
        self.page = page
        self.search_input = '#filter_keyword'
        self.search_dropdown_ul = '#search-category'
        self.add_to_cart_from_datasheet = 'ul.productpagecart a.cart'
        self.lip_search_viva_glam_link = 'a[title="Viva Glam Lipstick"]'
        self.add_to_cart_from_grid = 'a[data-id="59"].productcart'
        self.no_product_message_div = 'div:has-text("There is no product that matches the search criteria.")'
        self.search_button_header = 'div.button-in-search'
        self.thumbnails_grid = 'div.thumbnails.grid.row.list-inline'

    def search_product(self, keyword):
        self.page.wait_for_selector(self.search_input)
        self.page.click(self.search_input)
        self.page.fill(self.search_input, keyword)
        # Send Enter key to submit
        self.page.keyboard.press('Enter')

    def click_viva_glam_from_results(self):
        self.page.wait_for_selector(self.lip_search_viva_glam_link)
        self.page.click(self.lip_search_viva_glam_link)

    def add_to_cart_datasheet(self):
        self.page.wait_for_selector(self.add_to_cart_from_datasheet)
        self.page.click(self.add_to_cart_from_datasheet)

    def add_to_cart_from_search_results(self):
        self.page.wait_for_selector(self.add_to_cart_from_grid)
        self.page.click(self.add_to_cart_from_grid)

    def has_no_results_message(self):
        self.page.wait_for_selector(self.no_product_message_div)
        return self.page.is_visible(self.no_product_message_div)