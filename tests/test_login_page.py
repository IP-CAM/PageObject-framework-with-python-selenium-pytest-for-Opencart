import pytest
from pages.login_page import LoginPage
from utilites.read_properties import ReadConfig


class TestLogin:
    def test_guest_can_login_from_login_page(self, browser):
        url = ReadConfig.get_application_url()
        email = ReadConfig.get_application_email()
        password = ReadConfig.get_application_password()
        page = LoginPage(browser, url=url)
        page.open()
        page.should_be_login_page()
        page.login(email=email, password=password)
        page.should_be_authorized()
