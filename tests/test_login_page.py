import pytest
import allure
from pages.login_page import LoginPage
from utilites.read_properties import ReadConfig


# Test configs
existing_email = ReadConfig.get_application_email()
existing_password = ReadConfig.get_application_password()


class TestLogin:
    @allure.feature("Login")
    @allure.story("Login from login page with email and password")
    @allure.severity('blocker')
    def test_guest_can_login(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page_from_header()
        page.should_be_login_page()
        page.login()
        page.should_be_authorized()

    @allure.feature("Login")
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "email, password",
        [('', ''), (existing_email, ''),
         (existing_email, 'wrong_password'),
         ('notexisting@email.com', existing_password)]
    )
    def test_guest_can_login_negative(self, browser, email, password):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page_from_header()
        page.should_be_login_page()
        page.login_with_false_data(email, password)
        page.should_be_warning()

    @allure.story("Check urls from header")
    @allure.severity('critical')
    def test_guest_can_go_to(self, browser):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page_from_header()
        page.go_to_register_page_from_login_page()
        page.go_to_cart_page_from_header()
        page.go_to_contact_us_page_from_header()
        page.go_to_wishlist_page_from_header()
