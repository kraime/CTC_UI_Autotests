import logging
import time
from allure import step
from pages.base import Base
from locators.registration import RegistrationPageLocators
from faker import Faker


class RegistrationPage(Base):
    path = "auth/"

    @step
    def open_registration_page(self):
        self.browser.get(self.url + self.path)

    @step
    def click_to_register_tab(self):
        reg_tab = self._find_element(RegistrationPageLocators.REGISTER_TAB)
        reg_tab.click()

    @step
    def check_elements_on_registration_page(self):
        self._find_elements(RegistrationPageLocators.REGISTER_TAB)
        self._find_elements(RegistrationPageLocators.INPUT_EMAIL)
        self._find_elements(RegistrationPageLocators.INPUT_PASSWORD)
        self._find_elements(RegistrationPageLocators.REGISTRATION_BUTTON)

    @step
    def fill_data_in_registration_page(self):
        faker_email = Faker().email()

        input_email = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_EMAIL)
        self._input_text(input_email, faker_email)

        input_password = self._wait_element_to_be_clickable(RegistrationPageLocators.INPUT_PASSWORD)
        self._input_text(input_password, '123456')

    @step
    def click_to_registration_button(self):
        reg_button = self._find_element(RegistrationPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
        time.sleep(3)

    @step
    def check_successful_signup_modal(self):
        self._wait_element_to_be_presence(RegistrationPageLocators.MODAL_CONTENT)

    @step
    def check_successful_signup_modal_with_text(self):
        title_element = self._find_element(RegistrationPageLocators.SUCCESSFUL_SIGNUP_MODAL)
        assert title_element.text == 'СПАСИБО ЗА РЕГИСТРАЦИЮ!\nДля подтверждения аккаунта перейдите по ссылке в письме, отправленном на ваш email.'

    def close_modal_button(self):
        close_modal_button = self._find_element(RegistrationPageLocators.MODAL_CLOSE_BUTTON)
        close_modal_button.click()
        time.sleep(3)
