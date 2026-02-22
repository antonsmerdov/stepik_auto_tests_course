import pytest
from pages.product_page import ProductPage

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