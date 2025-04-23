class Product:
    def __init__(self, page):
        self.page = page
        # Header search bar
        self.search_input = 'form#search_form input#filter_keyword'
        # Lipstick Page
        self.add_to_cart_single = 'ul.productpagecart a.cart'
        # Lip search results
        self.lip_grid = 'div.thumbnails.grid'
        self.lipstick_result_link = 'a[title="Viva Glam Lipstick"]'
        # Link to cart from grid
        self.add_to_cart_result_grid = 'div.thumbnails.grid div[data-id="59"]'
        self.productcart_selector = 'a.productcart[data-id="59"]'
        # Lipstick datasheet page - Add to wishlist etc. not strictly used in test

        # No search result
        self.no_product_msg = 'div.contentpanel > div:has-text("There is no product that matches the search criteria.")'

    def search_and_open(self, term, open_first_match=False, open_exact_title=None):
        self.page.wait_for_selector(self.search_input, timeout=10000)
        self.page.fill(self.search_input, term)
        self.page.keyboard.press("Enter")
        if open_exact_title:
            self.page.wait_for_selector(self.lip_grid, timeout=10000)
            self.page.wait_for_selector(f'a[title="{open_exact_title}"]', timeout=10000)
            self.page.click(f'a[title="{open_exact_title}"]')
        elif open_first_match:
            self.page.wait_for_selector(self.lip_grid, timeout=10000)
            first_product = self.page.query_selector_all('div.thumbnails.grid a.prdocutname')[0]
            first_product.click()

    def click_add_to_cart_on_product(self):
        self.page.wait_for_selector(self.add_to_cart_single, timeout=10000)
        self.page.click(self.add_to_cart_single)

    def click_add_to_cart_from_grid_for_viva_glam(self):
        self.page.wait_for_selector(self.lip_grid, timeout=10000)
        self.page.wait_for_selector(self.productcart_selector, timeout=10000)
        self.page.click(self.productcart_selector)

    def assert_no_search_results(self):
        self.page.wait_for_selector('div.contentpanel', timeout=10000)
        try:
            self.page.wait_for_selector('div.contentpanel > div', timeout=3000, state="visible")
            text = self.page.inner_text('div.contentpanel > div')
            return 'no product that matches the search criteria' in text
        except:
            return False