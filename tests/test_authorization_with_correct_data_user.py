import pytest
from pages.AuthorizationPage import AuthorizationPage
import allure
from allure import step


@allure.feature('Авторизация юзера с корректными данными на сайте телеканала СТС')
@allure.title('Страница авторизации юзера')
def test_registration_user_with_correct_data(browser):
    authorization_page = AuthorizationPage(browser)
    with step("Открывает страницу Авторизации юзера"):
        authorization_page.open_authorization_page()
    with step("Tab Входа юзера"):
        authorization_page.click_to_login_tab()
    with step("Проверяет элементы на странице авторизации"):
        authorization_page.check_elements_on_authorization_page()
    with step("Заполняет данные полей для авторизации"):
        authorization_page.fill_data_in_authorization_page()
    with step("Производится click по кнопке Войти"):
        authorization_page.click_to_login_button()
    with step("Проверяет Title Главной страницы"):
        current_title = browser.title
        assert current_title == 'Телеканал СТС - официальный сайт'
