class Product:
    def __init__(self, page):
        self.page = page
        self.search_bar_selector = '.navbar-right .block_4 #search_form input#filter_keyword'
        self.viva_glam_lipstick_selector = 'a[title="Viva Glam Lipstick"]'
        self.add_to_cart_from_datasheet_selector = 'fieldset ul.productpagecart a.cart'
        self.add_to_cart_from_grid_template = 'a.productcart[data-id="{}"]'
        self.no_product_result_selector = 'div.contentpanel div:has-text("There is no product that matches the search criteria.")'
    
    def search_and_enter(self, text):
        self.page.wait_for_selector(self.search_bar_selector, timeout=15000)
        self.page.fill(self.search_bar_selector, text)
        self.page.keyboard.press('Enter')

    def select_lipstick_from_grid_by_title(self):
        self.page.wait_for_selector(self.viva_glam_lipstick_selector, timeout=15000)
        self.page.click(self.viva_glam_lipstick_selector)
    
    def click_add_to_cart_from_datasheet(self):
        self.page.wait_for_selector(self.add_to_cart_from_datasheet_selector, timeout=15000)
        self.page.click(self.add_to_cart_from_datasheet_selector)

    def click_add_to_cart_from_grid_by_id(self, product_id):
        selector = self.add_to_cart_from_grid_template.format(str(product_id))
        self.page.wait_for_selector(selector, timeout=15000)
        self.page.click(selector)

    def is_no_product_result_visible(self):
        try:
            self.page.wait_for_selector(self.no_product_result_selector, timeout=10000)
            return True
        except:
            return False