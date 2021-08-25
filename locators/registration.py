from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTER_TAB = (By.ID, "register-tab")
    INPUT_EMAIL = (By.ID, "email-input")
    INPUT_PASSWORD = (By.ID, "password-input")
    REGISTRATION_BUTTON = (By.ID, "register-btn")
    MODAL_CONTENT = (By.ID, "modal-content")
    SUCCESSFUL_SIGNUP_MODAL = (By.ID, "successful-signup-modal")
    MODAL_CLOSE_BUTTON = (By.ID, "modal-close-btn")
