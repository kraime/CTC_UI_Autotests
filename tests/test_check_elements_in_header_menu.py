import pytest
from pages.base import Base
from pages.HeadermenuPage import HeadermenuPage
import allure
from allure import step


@allure.feature('Проверка элементов меню в хедере')
@allure.title('Проверка элементов меню в хедере')
def test_check_elements_in_header_menu(browser):
    main_page = Base(browser)
    with step("Открывает Главную страницу сайта"):
        main_page.open_main_page()
    with step("Tab Входа юзера"):
        headermenu_page = HeadermenuPage
    with step("Проверка элемента Прямой Эфир в хедере"):
        headermenu_page.check_onair_element()
    with step("Проверка элемента Телепрограмма в хедере"):
        headermenu_page.check_teleprogramm_element()
    with step("Проверка элемента Шоу в хедере"):
        headermenu_page.check_show_element()
    with step("Проверка элемента Фильмы в хедере"):
        headermenu_page.check_films_element()
    with step("Проверка элемента Мультфильмы в хедере"):
        headermenu_page.check_multfilms_element()