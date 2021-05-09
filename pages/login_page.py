from locators.locators import LoginPageLocators
from pages.base_page import BasePage
from utilites.read_properties import ReadConfig


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert 'login' in self.browser.current_url

    def login(self, email, password):
        email_holder = self.browser.find_element(*LoginPageLocators.EMAIL_HOLDER)
        email_holder.clear()
        email_holder.send_keys(email)
        password_holder = self.browser.find_element(*LoginPageLocators.PASSWORD_HOLDER)
        password_holder.clear()
        password_holder.send_keys(password)
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_btn.click()

    def should_be_warning(self):
        self.is_element_present(*LoginPageLocators.LOGIN_WARNING_PASS_OR_EMAIL)

    def go_to_forgotten_password_1(self):
        forgotten_password_1 = self.browser.find_element(*LoginPageLocators.FORGOTTEN_PASS_1)
        forgotten_password_1.click()

    def go_to_register_page_from_login_page(self):
        continue_button = self.browser.find_element(*LoginPageLocators.REG_ACC_CONTINUE_BUTTON)
        continue_button.click()

    def go_to_login_page_from_login_table(self):
        login_cell = self.browser.find_element(*LoginPageLocators.LOGIN_CELL)
        login_cell.click()

    def go_to_register_page_from_login_table(self):
        register_cell = self.browser.find_element(*LoginPageLocators.REGISTER_CELL)
        register_cell.click()

    def go_to_forgotten_password_2(self):
        forgotten_password_2 = self.browser.find_element(*LoginPageLocators.FORGOTTEN_PASS_2)
        forgotten_password_2.click()

    def go_to_my_account_page_from_login_table(self):
        my_account = self.browser.find_element(*LoginPageLocators.MY_ACCOUNT_CELL)
        my_account.click()

    def should_be_authorized(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT_CELL), "Probably you ain't authorized"
