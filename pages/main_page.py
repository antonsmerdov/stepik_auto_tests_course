from pages.base_page import BasePage # Полный путь без точек
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def should_be_login_link(self):
        # Если элемента нет, сработает наше сообщение после запятой
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"