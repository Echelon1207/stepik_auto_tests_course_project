from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "'login' is not presented in current url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email, password):
        email_for_register = self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTER)
        email_for_register.send_keys(email)
        password_1_for_register = self.browser.find_element(*LoginPageLocators.PASSWORD_1_FOR_REGISTER)
        password_1_for_register.send_keys(password)
        password_2_for_register = self.browser.find_element(*LoginPageLocators.PASSWORD_2_FOR_REGISTER)
        password_2_for_register.send_keys(password)
        button_for_register = self.browser.find_element(*LoginPageLocators.BUTTON_FOR_REGISTER)
        button_for_register.click()
