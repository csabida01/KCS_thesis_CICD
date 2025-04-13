import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def set_up_fresh_browser():
    with sync_playwright() as sp:
        browser = sp.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def set_up_logged_in_browser():
    with sync_playwright() as sp:
        browser = sp.chromium.launch()
        context = browser.new_context(storage_state="logged_in_state.json")
        page = context.new_page()
        yield page
        browser.close()
