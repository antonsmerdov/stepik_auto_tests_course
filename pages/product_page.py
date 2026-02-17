from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        # Находим кнопку и нажимаем
        # Обязательно используй звездочку * для распаковки кортежа!
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    def should_be_message_about_adding(self):
        # Проверка: название товара в сообщении совпадает с тем, который добавляли
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message_product_name, f"Product name '{product_name}' does not match message '{message_product_name}'"

    def should_be_message_basket_total(self):
        # Проверка: стоимость корзины совпадает с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_price, f"Product price '{product_price}' does not match basket total '{basket_price}'"