class Product:
    def __init__(self, page):
        self.page = page

    # SEARCH
    def search(self, keyword):
        self.page.wait_for_selector('input#filter_keyword')
        self.page.click('input#filter_keyword')
        self.page.fill('input#filter_keyword', keyword)
        self.page.keyboard.press('Enter')

    # LIP SEARCH RESULTS
    def click_product_title(self, title_text):
        selector = f'a[title="{title_text}"]'
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    # LIPSTICK DATASHEET
    def add_to_cart_from_datasheet(self):
        self.page.wait_for_selector('ul.productpagecart a.cart')
        self.page.click('ul.productpagecart a.cart')

    # PRODUCT GRID: Add to Cart for Viva Glam Lipstick (id=59)
    def add_to_cart_from_search_result(self, product_id):
        add_cart_selector = f'a.productcart[data-id="{product_id}"]'
        self.page.wait_for_selector(add_cart_selector)
        self.page.click(add_cart_selector)

    # LIPSTICK NO FINDINGS
    def is_no_product_found(self):
        self.page.wait_for_selector('div.contentpanel > div')
        return self.page.inner_text('div.contentpanel > div').strip() == "There is no product that matches the search criteria."