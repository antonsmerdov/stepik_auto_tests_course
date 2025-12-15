import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 1. Добавляем параметры в настройки Pytest
def pytest_addoption(parser):
    # Ваш старый параметр для выбора браузера
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    # НОВЫЙ параметр для выбора языка
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, etc.")


# 2. Обновляем фикстуру browser
@pytest.fixture(scope="function")
def browser(request):
    # Считываем параметры из командной строки
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    browser = None

    # Логика выбора браузера и настройки языка
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language='{user_language}'..")

        # Настройка языка для Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with language='{user_language}'..")

        # Настройка языка для Firefox (если вдруг захотите проверить и там)
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)

        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()