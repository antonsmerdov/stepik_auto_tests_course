from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    sumbit_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    sumbit_button.click()

    browser.switch_to.window(browser.window_handles[1])

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
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()