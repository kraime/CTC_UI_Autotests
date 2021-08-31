from selenium.webdriver.common.by import By


class HeadermenuPageLocators:
    ONAIR = (By.ID, "https://ctc.ru/online/")
    TELEPROGRAMM = (By.ID, "/programm/")
    SHOW = (By.ID, "/collections/show/")
    FILMS = (By.ID, "/collections/filmi/")
    MULTFILMS = (By.ID, "/collections/multiki/")
