import logging
import time
from allure import step
from pages.base import Base
from locators.authorization import AuthorizationPageLocators
from utils.constants import Incorrect_email, Incorrect_pass


class AuthorizationPage(Base):
    path = "auth/"

    @step
    def open_authorization_page(self):
        self.browser.get(self.url + self.path)

    @step
    def click_to_login_tab(self):
        log_tab = self._find_element(AuthorizationPageLocators.LOGIN_TAB)
        log_tab.click()

    @step
    def check_elements_on_authorization_page(self):
        self._find_elements(AuthorizationPageLocators.LOGIN_TAB)
        self._find_elements(AuthorizationPageLocators.INPUT_EMAIL)
        self._find_elements(AuthorizationPageLocators.INPUT_PASSWORD)
        self._find_elements(AuthorizationPageLocators.LOGIN_BUTTON)

    @step
    def fill_data_in_authorization_page(self):
        input_email = self._wait_element_to_be_clickable(AuthorizationPageLocators.INPUT_EMAIL)
        self._input_text(input_email, 'idvurechenskij@ctcmedia.ru')

        input_password = self._wait_element_to_be_clickable(AuthorizationPageLocators.INPUT_PASSWORD)
        self._input_text(input_password, '123456')

    @step
    def fill_data_in_authorization_page_with_incorrect_email(self):
        input_email = self._wait_element_to_be_clickable(AuthorizationPageLocators.INPUT_EMAIL)
        self._input_text(input_email, Incorrect_email)

        input_password = self._wait_element_to_be_clickable(AuthorizationPageLocators.INPUT_PASSWORD)
        self._input_text(input_password, '123456')

    @step
    def fill_data_in_authorization_page_with_incorrect_password(self):
        input_email = self._wait_element_to_be_clickable(AuthorizationPageLocators.INPUT_EMAIL)
        self._input_text(input_email, 'idvurechenskij@ctcmedia.ru')

        input_password = self._wait_element_to_be_clickable(AuthorizationPageLocators.INPUT_PASSWORD)
        self._input_text(input_password, Incorrect_pass)

    @step
    def click_to_login_button(self):
        login_button = self._find_element(AuthorizationPageLocators.LOGIN_BUTTON)
        login_button.click()
        time.sleep(3)

    @step
    def check_autorization_error_text(self):
        error_element = self._find_element(AuthorizationPageLocators.AUTORIZATION_ERROR_TEXT)
        assert error_element.text == 'Проверьте корректность email или пароля.'
