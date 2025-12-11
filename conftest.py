import pytest
from selenium import webdriver


# 1. Добавляем параметр --browser_name в настройки Pytest
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


# 2. Обновляем фикстуру browser
@pytest.fixture(scope="function")
def browser(request):
    # Считываем значение параметра из командной строки
    browser_name = request.config.getoption("browser_name")

    browser = None

    # Логика выбора браузера
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        # Если передали что-то странное (например, --browser_name=yandex)
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()