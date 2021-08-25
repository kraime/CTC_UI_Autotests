from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    LOGIN_TAB = (By.ID, "login-tab")
    INPUT_EMAIL = (By.ID, "email-input")
    INPUT_PASSWORD = (By.ID, "password-input")
    LOGIN_BUTTON = (By.ID, "login-btn")
    AUTORIZATION_ERROR_TEXT = (By.ID, "authorization-error-text")
