from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Кликаем на кнопку, запускающую alert (Назвали кнопку)
    start_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    start_button.click()

    # 2. Принимаем alert
    browser.switch_to.alert.accept()

    # 3. Ждем, пока появится поле со значением X (Оставляем только один поиск!)
    x_value_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )

    # 4. Получаем текст X и сразу преобразуем его в число
    x_text = x_value_element.text
    x_value = int(x_text)
    print(f"Значение X: {x_value}")

    # 5. Считаем формулу (Используем x_value)
    # math.log(abs(12 * math.sin(x_value)))
    result_float = math.log(abs(12 * math.sin(x_value)))
    result_string = str(result_float)
    print(f"Результат формулы: {result_string}")

    # 6. Вводим результат в поле ответа (Назвали поле)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result_string)

    # 7. Кликаем кнопку Submit (Назвали кнопку и убедились, что она есть)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()