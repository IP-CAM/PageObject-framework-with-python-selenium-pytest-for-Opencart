from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from locators.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url='http://localhost', timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_disappeared(self, how, what, timeout=5):
        # 1 - Poll frequency(sleep interval between calls),
        # TimeoutException - iterable structure of exception classes ignored during calls
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized(self):
        self.browser.find_element(*BasePageLocators.MY_ACCOUNT_BUTTON_DROPDOWN).click()
        assert self.is_element_present(*BasePageLocators.MY_ACCOUNT_MY_ACCOUNT_BUTTON), "Probably you aint authorized"


    def go_to_contact_us_page_from_header(self):
        contact_us = self.browser.find_element(*BasePageLocators.CONTACT_US_BUTTON)
        contact_us.click()

    def go_to_register_page_from_header(self):
        account_dropdown = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_BUTTON_DROPDOWN)
        account_dropdown.click()
        register = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_REGISTER_BUTTON)
        register.click()

    def go_to_login_page_from_header(self):
        account_dropdown = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_BUTTON_DROPDOWN)
        account_dropdown.click()
        login = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_LOGIN_BUTTON)
        login.click()

    # Only for authorized user! Otherwise redirect to login page!
    def go_to_wishlist_page_from_header(self):
        wishlist = self.browser.find_element(*BasePageLocators.WISH_LIST_BUTTON)
        wishlist.click()

    def go_to_cart_page_from_header(self):
        cart = self.browser.find_element(*BasePageLocators.CART_ICON_BUTTON)
        cart.click()

    # Only when there is some product in the cart! Otherwise redirect to cart!
    def go_to_checkout_page_from_header(self):
        checkout = self.browser.find_element(*BasePageLocators.CHECKOUT_BUTTON)
        checkout.click()
