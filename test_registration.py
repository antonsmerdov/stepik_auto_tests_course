import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Этот метод запускается перед каждым тестом
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # Этот метод запускается после каждого теста (закрывает браузер)
        self.browser.quit()

    def test_registration1(self):
        # Тест для первой страницы (должен пройти успешно)
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Код заполнения полей для первой страницы
        input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("Smolensk")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        time.sleep(1)

        # Проверяем результат
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверяем с помощью unittest
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        # Тест для второй страницы
        # ОН ДОЛЖЕН УПАСТЬ С ОШИБКОЙ NoSuchElementException, так задумано заданием!
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Пытаемся использовать те же селекторы, что и в первом тесте
        input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("Smolensk")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()