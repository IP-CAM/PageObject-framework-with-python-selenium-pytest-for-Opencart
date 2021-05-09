from locators.locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def should_be_register_page(self):
        assert 'register' in self.browser.current_url

    def register(self, first_name, last_name, email, telephone, password):
        first_name_holder = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_HOLDER)
        first_name_holder.clear()
        first_name_holder.send_keys(first_name)
        last_name_holder = self.browser.find_element(*RegisterPageLocators.LAST_NAME_HOLDER)
        last_name_holder.clear()
        last_name_holder.send_keys(last_name)
        email_holder = self.browser.find_element(*RegisterPageLocators.EMAIL_HOLDER)
        email_holder.clear()
        email_holder.send_keys(email)
        telephone_holder = self.browser.find_element(*RegisterPageLocators.TELEPHONE_HOLDER)
        telephone_holder.clear()
        telephone_holder.send_keys(telephone)
        password_holder = self.browser.find_element(*RegisterPageLocators.PASSWORD_HOLDER)
        password_holder.clear()
        password_holder.send_keys(password)
        password_confirm_holder = self.browser.find_element(*RegisterPageLocators.PASSWORD_CONFIRM_HOLDER)
        password_confirm_holder.clear()
        password_confirm_holder.send_keys(password)
        privacy_policy_check = self.browser.find_element(*RegisterPageLocators.PRIVACY_POLICE_CHECK_FIELD)
        privacy_policy_check.click()
        confirm_button = self.browser.find_element(*RegisterPageLocators.CONFIRM_BUTTON)
        confirm_button.click()
