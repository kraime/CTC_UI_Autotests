import time
import logging
from allure import step
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    url = "https://ctc-web-stage.dev.ctc.ru/"

    def __init__(self, browser):
        self.browser: WebDriver = browser

    @step
    def get_title(self, url):
        self.browser.get(url)

    @step
    def _input_text(self, element, text):
        element.clear()
        element.click()
        element.send_keys(text)

    @step
    def _find_elements(self, locator):
        return self.browser.find_elements(*locator)

    @step
    def _find_element(self, locator):

        WebDriverWait(self.browser, 4).until(
            EC.presence_of_element_located(locator)
        )

        return self.browser.find_element(*locator)
        # browser = Browser(Config(
        #     driver=self.browser))
        # return browser.element(*locator)

    @step
    def _wait_element_to_be_presence(self, locator, wait_time=4):
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            element = wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'{element} not found')
        return element

    @step
    def _wait_element_to_be_clickable(self, locator, wait_time=5):
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f'{locator} not clickable')
        return element
