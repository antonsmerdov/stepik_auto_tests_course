import math

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

drop_watcher = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button_book = browser.find_element(By.ID, "book")
button_book.click()


# 3. Ждем, пока появится поле со значением X (Оставляем только один поиск!)
x_value_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "input_value"))
)

# 4. Получаем текст X и сразу преобразуем его в число
x_text = x_value_element.text
x_value = int(x_text)

# 5. Считаем формулу (Используем x_value)
# math.log(abs(12 * math.sin(x_value)))
result_float = math.log(abs(12 * math.sin(x_value)))
result_string = str(result_float)

# 6. Вводим результат в поле ответа (Назвали поле)
answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(result_string)

# 7. Кликаем кнопку Submit (Назвали кнопку и убедились, что она есть)
submit_button = browser.find_element(By.ID, "solve")
submit_button.click()

time.sleep(100)