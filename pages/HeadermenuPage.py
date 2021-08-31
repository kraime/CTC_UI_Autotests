import logging
import time
from allure import step
from pages.base import Base
from locators.header_menu_elements import HeadermenuPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeadermenuPage(Base):

    @step
    def check_onair_element(self):
        self._find_elements(HeadermenuPageLocators.https://ctc.ru/online/)

    @step
    def check_teleprogramm_element(self):
        self._find_elements(HeadermenuPageLocators./programm/)

    @step
    def check_show_element(self):
        self._find_elements(HeadermenuPageLocators.["/collections/show/"])

    @step
    def check_films_element(self):
        self._find_elements(HeadermenuPageLocators.["/collections/filmi/"])

    @step
    def check_multfilms_element(self):
        self._find_elements(HeadermenuPageLocators.["/collections/multiki/"])
