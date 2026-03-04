from pages.main_page import MainPage
from pages.login_page import LoginPage  # 1. Добавляем импорт страницы логина
from pages.basket_page import BasketPage  # Не забудь импортировать!

import pytest



# Вешаем метку на ВЕСЬ класс. Теперь она сработает для всех тестов внутри.
@pytest.mark.login_guest
class TestLoginFromMainPage():

    # ВАЖНО: не забудь добавить слово self первым аргументом,
    # так как теперь это метод класса, а не просто функция!
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# Если у тебя в этом файле остался тест корзины (test_guest_cant_see_product_in_basket_opened_from_main_page),
# оставь его снаружи класса, так как он не относится к логину.

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()  # Переходим в корзину

    # Инициализируем страницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()  # Проверяем, что нет товаров
    basket_page.should_be_empty_basket_message()  # Проверяем текст


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # Инициализируем MainPage
    page = MainPage(browser, link)
    page.open()  # Открываем страницу
    page.go_to_login_page()  # Выполняем клик

    # 2. Инициализируем LoginPage, передавая текущий url браузера
    login_page = LoginPage(browser, browser.current_url)

    # 3. Проверяем, что URL верный и формы на месте
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  #
    page.open()  #
    page.should_be_login_link()  #
