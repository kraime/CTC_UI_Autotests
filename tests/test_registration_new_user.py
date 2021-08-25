import pytest
from pages.RegistrationPage import Faker
from pages.RegistrationPage import RegistrationPage
import allure
from allure import step


@allure.feature('Регистрация нового юзера на сайте телеканала СТС')
@allure.title('Страница регистрации нового юзера')
def test_registration_new_user(browser):
    registration_page = RegistrationPage(browser)
    with step("Открывает страницу регистрации нового юзера"):
        registration_page.open_registration_page()
    with step("Происходит переключение на Tab Регистрации"):
        registration_page.click_to_register_tab()
    with step("Проверяет элементы на странице регистрации"):
        registration_page.check_elements_on_registration_page()
    with step("Заполняет данные полей для регистрации"):
        registration_page.fill_data_in_registration_page()
    with step("Производится click по кнопке Зарегистрироваться"):
        registration_page.click_to_registration_button()
    with step("Производится поиск модалки успешной регистрации"):
        registration_page.check_successful_signup_modal()
    with step("Производится поиск текста об успешной регистрации пользователя"):
        registration_page.check_successful_signup_modal_with_text()
    with step("Производится закрытие модального окна"):
        registration_page.close_modal_button()
