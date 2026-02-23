from pages.base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    # 1. Этот метод мы используем для КЛИКА (чтобы перейти)
    def go_to_login_page(self):
        # Находим элемент по локатору и кликаем
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # 2. Этот метод мы используем для ПРОВЕРКИ (чтобы увидеть ссылку)
    def should_be_login_link(self):
        # Проверяем наличие элемента через наш детектор из BasePage
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
