import math  # <--- Добавь это в начало файла!
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException  # <--- Добавь NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        # Добавляем новый метод решения задачки

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        # Метод ждет появления элемента в течение timeout секунд.
        # Если элемент так и НЕ ПОЯВИЛСЯ, падает TimeoutException.
        # Мы ловим эту ошибку и возвращаем True (всё ок, элемента нет).
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        # Если элемент появился, код дойдет сюда, и мы вернем False (тест упадет).
        return False

    def is_disappeared(self, how, what, timeout=4):
        # Метод ждет, пока элемент НЕ ИСЧЕЗНЕТ (until_not) в течение timeout секунд.
        # Если он исчез вовремя, мы возвращаем True.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            # Если время вышло, а элемент всё еще торчит на экране - возвращаем False.
            return False

        return True
