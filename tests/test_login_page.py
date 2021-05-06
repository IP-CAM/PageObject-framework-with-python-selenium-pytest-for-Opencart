import pytest
from pages.login_page import LoginPage


class TestLogin:
    def test_guest_can_login(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page_from_header()
        page.should_be_login_page()
        page.login()
        page.should_be_authorized()

    def test_guest_can_go_to(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page_from_header()
        page.go_to_register_page_from_login_page()
        page.go_to_cart_page_from_header()
        page.go_to_contact_us_page_from_header()
        page.go_to_wishlist_page_from_header()