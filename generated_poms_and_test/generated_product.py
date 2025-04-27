class Product:
    # Selectors for product searching and product page
    # Use "a[title='Viva Glam Lipstick']" for searching by exact product in the grid
    VIVA_GLAM_LIPSTICK_LINK = 'a[title="Viva Glam Lipstick"]'
    ADD_TO_CART_ON_DATASHEET = 'ul.productpagecart a.cart'
    # On search grid, buttons are like 'a.productcart[data-id="59"]' for Viva Glam Lipstick,
    # but add to cart not on grid for "Lipstick" exact

    # Wishlist selectors
    WISHLIST_ADD = 'a.wishlist_add.btn'
    WISHLIST_REMOVE = 'a.wishlist_remove.btn'

    @staticmethod
    def click_viva_glam_lipstick_from_search(page):
        page.wait_for_selector(Product.VIVA_GLAM_LIPSTICK_LINK, timeout=15000)
        page.click(Product.VIVA_GLAM_LIPSTICK_LINK)

    @staticmethod
    def add_to_cart_from_datasheet(page):
        page.wait_for_selector(Product.ADD_TO_CART_ON_DATASHEET, timeout=15000)
        page.click(Product.ADD_TO_CART_ON_DATASHEET)

    @staticmethod
    def add_first_product_to_cart_from_search(page):
        # "Add to Cart" for Viva Glam Lipstick on search grid
        add_to_cart_btn = 'a.productcart[data-id="59"]'
        page.wait_for_selector(add_to_cart_btn, timeout=15000)
        page.click(add_to_cart_btn)

    @staticmethod
    def is_no_results_message(page):
        # "There is no product that matches the search criteria."
        selector = "div.contentpanel > div:has-text('There is no product that matches the search criteria.')"
        try:
            page.wait_for_selector(selector, timeout=15000)
            return page.is_visible(selector)
        except:
            return False