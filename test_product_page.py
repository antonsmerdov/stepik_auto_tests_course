from pages.product_page import ProductPage
import pytest

# Ссылка с промо-акцией
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # Инициализируем Page Object
    page.open()  # Открываем страницу
    page.add_product_to_basket()  # Жмем кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()  # Решаем задачку в алерте (метод из BasePage)

    # Запускаем проверки
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()