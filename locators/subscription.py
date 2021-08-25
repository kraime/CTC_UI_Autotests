from selenium.webdriver.common.by import By


class SubscriptionPageLocators:
    SUBSCRIPTION_HEADER_BUTTON = (By.ID, "subscription-header-btn")
    BUY_SUBSCRIPTION_BUTTON = (By.ID, "buy-subscription-btn")
    PAYMENT_MODAL = (By.ID, "payment-modal")
    CARD_NUMBER = (By.CSS_SELECTOR, "input[name='PAN']")
    MONTH = (By.CSS_SELECTOR, "input[name='EMonth']")
    YEAR = (By.CSS_SELECTOR, "input[name='EYear']")
    CVV = (By.CSS_SELECTOR, "input[name='cvv']")
    BUY_SUBSCRIPTION_BUTTON_MAP_FORM = (By.XPATH, "//button[text()='ПОДПИСАТЬСЯ И СМОТРЕТЬ']")
    SUBSCRIPTION_SUCCESS_BUTTON = (By.ID, "subscription-success-btn")
    PAYMENT_IFRAME = (By.CSS_SELECTOR, "#payment-modal iframe")
