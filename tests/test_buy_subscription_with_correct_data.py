import pytest
from pages.RegistrationPage import Faker
from pages.RegistrationPage import RegistrationPage
from pages.SubscriptionPage import SubscriptionPage
import allure
from allure import step


@allure.feature('Регистрация нового юзера + Покупка подписки')
@allure.title('Страница регистрации нового юзера + Покупка подписки')
def test_registration_new_user_with_buy_subscription(browser):
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
    with step("Производится поиск формы при успешной регистрации"):
        registration_page.check_successful_signup_modal()
    with step("Закрывает модальное окно регистрации"):
        registration_page.close_modal_button()
        subscription_page = SubscriptionPage(browser)
    with step("Происходит клик по кнопке покупки подписки в хедере"):
        subscription_page.click_to_subscription_header_button()
    with step("Происходит проверка наличия модального окна с информацией о подписке"):
        subscription_page.check_payment_modal()
    with step("Происходит клик по кнопке покупки подписки в модальном окне"):
        subscription_page.click_to_buy_subscription_button()
    with step("Происходит переключение на MAP iframe"):
        subscription_page.switch_to_map_iframe()
    with step("Заполнение полей платежной карты"):
        subscription_page.fill_data_in_subscription_modal()
    with step("Происходит клик по кнопке покупки подписки на маповской форме"):
        subscription_page.click_to_buy_subscription_button_map_form()
    with step("Происходит переключение на CTC HTML"):
        subscription_page.switch_to_ctc_body()
    with step("Происходит поиск кнопки Перейти к просмотру"):
        subscription_page.check_subscription_success_button()
    with step("Происходит проверка Title страницы сайта"):
        current_title = browser.title
        assert current_title == 'Телеканал СТС - официальный сайт'
