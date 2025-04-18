import pytest
import os
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
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    storage_path = os.path.join(project_root, "logged_in_state.json")
    with sync_playwright() as sp:
        browser = sp.chromium.launch()
        context = browser.new_context(storage_state=storage_path)
        page = context.new_page()
        yield page
        browser.close()
