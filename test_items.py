import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)

    # Ищем кнопку "Добавить в корзину"
    # Селектор .btn-add-to-basket универсален для всех языков
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверяем, что список кнопок не пуст
    assert len(buttons) > 0, "Кнопка добавления в корзину не найдена!"