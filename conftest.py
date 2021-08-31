import os
import pytest
import logging
import allure
from selenium import webdriver
from utils.allure_helper import AllureCatchLogs
from webdriver_manager.chrome import ChromeDriverManager

# DRIVERS = os.path.expanduser("~/Drivers")


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption('--local', help='local or CI?', choices=['true', 'false'], default='true')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    """Pytest setup before each test."""
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    """Allure hook."""
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    """Pytest teardown after each test."""
    with AllureCatchLogs():
        yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Данный код помещает скриншот в отчет allure при падениях"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(scope='function')
def browser(request):
    """Фикстура для запуска браузеров локально и удаленно"""
    local = request.config.getoption("--local")
    if local != 'true' and local != 'false':
        raise ValueError(f'--local={local}". Driver could not be setup.\n'
                         'pass "true" if local execute\n'
                         'pass "false" if use CI service')

    driver = None
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--enable-automation")

    if local == 'true':
        driver = webdriver.Chrome(
            options=chrome_options,
            executable_path=ChromeDriverManager().install()
        )
    elif local == 'false':
        driver = webdriver.Remote(
            options=chrome_options,
            command_executor='http://selenium__standalone-chrome:4444/wd/hub'
        )

    driver.set_window_size(1920, 1600)
    # driver.implicitly_wait(5)
    logger = logging.getLogger('BrowserLogger')
    logger.info('Browser {} started'.format(browser))

    yield driver
    driver.quit()
