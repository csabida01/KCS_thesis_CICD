import pytest
from generated_loginPage import LoginPage
from generated_product import Product
from generated_cart import Cart
import time

BASE_URL = "https://automationteststore.com/"

def wait_for_elem_by_selector(page, selector, to_appear=True, timeout=12000):
    if to_appear:
        page.locator(selector).wait_for(state='visible', timeout=timeout)
    else:
        page.locator(selector).wait_for(state='detached', timeout=timeout)