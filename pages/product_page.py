from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    # --- Новые методы-помощники (вытаскивают данные) ---
    def get_product_name(self):
        # Находим элемент с названием и возвращаем его текст
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        # Находим элемент с ценой и возвращаем его текст
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # --- Методы-проверки (используют помощников) ---
    def should_be_message_about_adding(self):
        # 1. Запоминаем имя товара, который мы видим на экране
        product_name = self.get_product_name()

        # 2. Находим текст в сообщении об успехе
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

        # 3. Сравниваем (Динамически!)
        assert product_name == message_product_name, \
            f"Product name '{product_name}' does not match message '{message_product_name}'"

    def should_be_message_basket_total(self):
        # 1. Запоминаем цену товара
        product_price = self.get_product_price()

        # 2. Находим цену в сообщении корзины
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

        # 3. Сравниваем
        assert product_price == basket_price, \
            f"Product price '{product_price}' does not match basket total '{basket_price}'"