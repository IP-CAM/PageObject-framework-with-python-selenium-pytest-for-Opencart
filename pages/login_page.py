from locators.locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        assert 'login' in self.browser.current_url

    def login(self, email:str, password:str):
        email_holder = self.browser.find_element(*LoginPageLocators.EMAIL_HOLDER)
        email_holder.clear()
        email_holder.send_keys(email)
        password_holder = self.browser.find_element(*LoginPageLocators.PASSWORD_HOLDER)
        password_holder.clear()
        password_holder.send_keys(password)
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_btn.click()

    def go_to_forgotten_password_1(self):
        forgotten_password_1 = self.browser.find_element(*LoginPageLocators.FORGOTTEN_PASS_1)
        forgotten_password_1.click()

    def go_to_forgotten_password_2(self):
        forgotten_password_2 = self.browser.find_element(*LoginPageLocators.FORGOTTEN_PASS_2)
        forgotten_password_2.click()

    def go_to_register_page_from_login_page(self):
        continue_button = self.browser.find_element(*LoginPageLocators.REG_ACC_CONTINUE_BUTTON)
        continue_button.click()


