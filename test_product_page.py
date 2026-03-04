import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage  # Не забудь импортировать!
import time
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail(reason="Так задумано: сообщение появляется после добавления")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # Проверяем, что сообщения нет (а оно появится, поэтому тест упадет и это ок)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    # Просто открыли страницу и сразу проверяем, что сообщения нет (тест пройдет)
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Так задумано: сообщение не исчезает само")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # Ждем, что сообщение исчезнет (а оно не исчезнет, тест упадет по таймауту)
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # 2. Открываем страницу
    page.open()
    # 3. Выполняем метод перехода на страницу логина
    # (ProductPage берет этот метод из BasePage, так как унаследовал его)
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()  # Переходим в корзину

    # Инициализируем страницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()  # Проверяем, что нет товаров
    basket_page.should_be_empty_basket_message()  # Проверяем текст


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # 1. Открываем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()

        # 2. Генерируем уникальный email с помощью времени и задаем пароль
        email = str(time.time()) + "@fakemail.org"
        password = "TestPassword12345!"

        # 3. Регистрируем пользователя
        page.register_new_user(email, password)

        # 4. Проверяем, что пользователь залогинен
        page.should_be_authorized_user()

    # Переносим сюда тесты и меняем guest на user
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        # Тут твои проверки успешного добавления (названия и цены)
