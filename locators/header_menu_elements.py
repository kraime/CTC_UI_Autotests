from selenium.webdriver.common.by import By


class HeadermenuPageLocators:
    HEADER_CONTAINER = (By.ID, "header-links-container")
    HEADER_LINKS = (By.CSS_SELECTOR, "#header-links-container > li")
