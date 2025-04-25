class Product:
    def __init__(self, page):
        self.page = page

    # Search bar
    def fill_search_bar(self, query):
        self.page.wait_for_selector('#filter_keyword', timeout=10000)
        self.page.fill('#filter_keyword', query)

    def press_enter_search(self):
        self.page.keyboard.press("Enter")

    # Results page: select product by title (Viva Glam Lipstick)
    def click_product_by_title(self, title):
        locator = f'a[title="{title}"]'
        self.page.wait_for_selector(locator, timeout=10000)
        self.page.click(locator)

    # Add to cart in detailed product page
    def click_add_to_cart_from_details(self):
        self.page.wait_for_selector('ul.productpagecart a.cart', timeout=10000)
        self.page.click('ul.productpagecart a.cart')

    # Add to cart from grid by product id (e.g. data-id="59")
    def click_add_to_cart_from_grid(self, product_id):
        selector = f'div.pricetag.jumbotron a.productcart[data-id="{product_id}"]'
        self.page.wait_for_selector(selector, timeout=10000)
        self.page.click(selector)

    # No results in search
    def is_no_products_message_visible(self):
        return self.page.is_visible('div.contentpanel >> text="There is no product that matches the search criteria."')