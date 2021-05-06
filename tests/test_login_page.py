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
