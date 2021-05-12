import pytest
import allure
from pages.login_page import LoginPage
from utilites.read_properties import ReadConfig
from utilites.custom_logger import LogGen


class TestLogin:
    # Test configs
    existing_email = ReadConfig.get_application_email()
    valid_password = ReadConfig.get_application_password()

    logger = LogGen.log_generator()

    @allure.feature("Login")
    @allure.story("Login from login page with email and password")
    @allure.severity('blocker')
    @pytest.mark.parametrize(
        "email,password",
        [(existing_email, valid_password)])
    def test_guest_can_login(self, browser, email, password):
        self.logger.info("********* TestLogin *********")
        self.logger.info("********* Verifying 'Test guest can login' *********")
        page = LoginPage(browser)
        page.open()
        self.logger.info("********* Open main page *********")
        page.go_to_login_page_from_header()
        self.logger.info("********* Move to login page *********")
        page.should_be_login_page()
        self.logger.info("********* Try to login with existing email and valid password *********")
        page.login(email, password)
        page.should_be_authorized()
        self.logger.info("********* Authorization is successful *********")
        self.logger.info("********* Test guest can login is passed *********")

    @allure.feature("Login")
    @allure.severity('critical')
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "email,password",
        [('', ''), (existing_email, ''),
         (existing_email, 'wrong_password'),
         ('notexisting@email.com', valid_password)]
    )
    def test_guest_can_login_negative(self, browser, email, password):
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page_from_header()
        page.should_be_login_page()
        page.login(email, password)
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
