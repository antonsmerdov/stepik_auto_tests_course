import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage  # Не забудь импортировать!

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
