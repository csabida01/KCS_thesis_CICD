class Product:
    def __init__(self, page):
        self.page = page
        # Lipstick search grid selector and product selector
        self.lipstick_grid_selector = "a[title='Viva Glam Lipstick']"
        # From lipstick datasheet (Lipstick product details page)
        self.add_to_cart_selector = "ul.productpagecart li a.cart"

    def click_viva_glam_lipstick(self):
        self.page.wait_for_selector(self.lipstick_grid_selector, timeout=10000)
        self.page.click(self.lipstick_grid_selector)

    def add_to_cart(self):
        self.page.wait_for_selector(self.add_to_cart_selector, timeout=10000)
        self.page.click(self.add_to_cart_selector)