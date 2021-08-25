import logging
import time
from allure import step
from pages.base import Base
from locators.subscription import SubscriptionPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SubscriptionPage(Base):
    path = "payment/?redirect-url=/"

    @step
    def open_subscripton_page(self):
        self.browser.get(self.url + self.path)

    @step
    def click_to_subscription_header_button(self):
        subscription_head_button = self._find_element(SubscriptionPageLocators.SUBSCRIPTION_HEADER_BUTTON)
        subscription_head_button.click()

    @step
    def check_payment_modal(self):
        self._find_elements(SubscriptionPageLocators.PAYMENT_MODAL)

    @step
    def click_to_buy_subscription_button(self):
        subscription_button = self._find_element(SubscriptionPageLocators.BUY_SUBSCRIPTION_BUTTON)
        subscription_button.click()

    @step
    def switch_to_map_iframe(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(SubscriptionPageLocators.PAYMENT_IFRAME)
        )
        self.browser.switch_to.frame(self._find_element(SubscriptionPageLocators.PAYMENT_IFRAME))

    @step
    def switch_to_ctc_body(self):
        self.browser.switch_to.default_content()

    @step
    def fill_data_in_subscription_modal(self):
        input_card_number = self._wait_element_to_be_clickable(SubscriptionPageLocators.CARD_NUMBER)
        self._input_text(input_card_number, '4111 1111 1111 1111')

        input_month = self._wait_element_to_be_clickable(SubscriptionPageLocators.MONTH)
        self._input_text(input_month, '12')

        input_year = self._wait_element_to_be_clickable(SubscriptionPageLocators.YEAR)
        self._input_text(input_year, '21')

        input_cvv = self._wait_element_to_be_clickable(SubscriptionPageLocators.CVV)
        self._input_text(input_cvv, '123')

    @step
    def click_to_buy_subscription_button_map_form(self):
        subscription_button_map_form = self.browser.find_element_by_css_selector("button[tabindex='5'")
        subscription_button_map_form.click()
        time.sleep(3)

    @step
    def check_subscription_success_button(self):
        self._find_element(SubscriptionPageLocators.SUBSCRIPTION_SUCCESS_BUTTON)
