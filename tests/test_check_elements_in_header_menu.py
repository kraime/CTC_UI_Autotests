import pytest
from pages.base import Base
from pages.HeadermenuPage import HeadermenuPage
import allure
from allure import step


@allure.feature('Проверка элементов меню в хедере')
@allure.title('Проверка элементов меню в хедере')
def test_check_elements_in_header_menu(browser):
    headermenu_page = HeadermenuPage(browser)
    with step("Проверяет контейнер в хеддере"):
        headermenu_page.check_header_container()
    with step("Проверяет кол-во ссылок в хеддере"):
        headermenu_page.check_header_links()
