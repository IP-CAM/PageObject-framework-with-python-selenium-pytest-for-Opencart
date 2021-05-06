import pytest
from pages.login_page import LoginPage
from utilites.read_properties import ReadConfig


class TestLogin:
    url = ReadConfig.get_application_url()
    email = ReadConfig.get_application_email()
    password = ReadConfig.get_application_password()

    def test_guest_can_login_from_login_page(self, browser, url, email, password):
        page = LoginPage(browser, url)
        page.open()
        page.should_be_login_page()
        page.login(email, password)
        page.should_be_authorized()
