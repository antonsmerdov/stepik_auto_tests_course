from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elemen_one_x = browser.find_element(By.ID, "input_value")
    x = int(elemen_one_x.text)
    print(x)

    result = str(math.log(abs(12*math.sin(int(x)))))
    print(result)

    button = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(result)

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3000)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
