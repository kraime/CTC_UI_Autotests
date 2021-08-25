import pytest
from pages.AuthorizationPage import AuthorizationPage
import allure
from allure import step


@allure.feature('Авторизация юзера на сайте телеканала СТС с некорректным имейлом')
@allure.title('Страница авторизации юзера с некорректным Email')
def test_autorization_with_incorrect_email(browser):
    authorization_page = AuthorizationPage(browser)
    with step("Открывает страницу Авторизации юзера"):
        authorization_page.open_authorization_page()
    with step("Tab Входа юзера"):
        authorization_page.click_to_login_tab()
    with step("Проверяет элементы на странице авторизации"):
        authorization_page.check_elements_on_authorization_page()
    with step("Заполняет данные полей для авторизации с некорректным Email"):
        authorization_page.fill_data_in_authorization_page_with_incorrect_email()
    with step("Производится click по кнопке Войти"):
        authorization_page.click_to_login_button()
    with step("Производится проверка текста ошибки в модальном окне"):
        authorization_page.check_autorization_error_text()
