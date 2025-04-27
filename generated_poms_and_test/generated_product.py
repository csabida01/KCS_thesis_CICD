class Product:
    def __init__(self, page):
        self.page = page

    @property
    def search_bar_input(self):
        return self.page.locator('input#filter_keyword')

    @property
    def lipstick_color_select(self):
        return self.page.locator('select#option305')

    @property
    def lipstick_add_to_cart(self):
        return self.page.locator('ul.productpagecart > li > a.cart')

    @property
    def grid_viva_glam_lipstick(self):
        return self.page.locator('a.prdocutname[title="Viva Glam Lipstick"]')

    @property
    def search_button(self):
        return self.page.locator('button#search_button')

    @property
    def no_product_found_text(self):
        return self.page.locator('div:has-text("There is no product that matches the search criteria.")')

    @property
    def product_grid_add_to_cart(self):
        # This grabs the "Add to Cart" for product_id=59 in grid search
        return self.page.locator('a.productcart[data-id="59"]')

    def search_for(self, query):
        self.search_bar_input.wait_for(state='visible')
        self.search_bar_input.click()
        self.search_bar_input.fill(query)
        self.search_bar_input.press('Enter')

    def click_viva_glam_lipstick_from_grid(self):
        self.grid_viva_glam_lipstick.wait_for(state='visible')
        self.grid_viva_glam_lipstick.click()

    def click_grid_add_to_cart(self):
        self.product_grid_add_to_cart.wait_for(state='visible')
        self.product_grid_add_to_cart.click()

    def lipstick_datasheet_add_to_cart(self):
        self.lipstick_add_to_cart.wait_for(state='visible')
        self.lipstick_add_to_cart.click()

    def no_results_text_present(self):
        self.no_product_found_text.wait_for(state='visible')
        return self.no_product_found_text.is_visible()