import logging
import time
from allure import step
from pages.base import Base
from locators.header_menu_elements import HeadermenuPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeadermenuPage(Base):
    path = "/"

    @step
    def check_header_container(self):
        self._find_elements(HeadermenuPageLocators.HEADER_CONTAINER)

    @step
    def check_header_links(self):
        header_links = self._find_elements(HeadermenuPageLocators.HEADER_LINKS)
        assert len(header_links) == 10

