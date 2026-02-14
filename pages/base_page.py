from selenium.common.exceptions import NoSuchElementException # ВАЖНО: импортируем ошибку
from selenium.webdriver.common.by import By

class BasePage():
    # Добавляем timeout для неявного ожидания
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # Наш новый метод-проверка
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True