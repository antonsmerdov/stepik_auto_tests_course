from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elemen_one = browser.find_element(By.ID, "num1")
    first_number = int(elemen_one.text)

    elemen_two = browser.find_element(By.ID, "num2")
    second_number = int(elemen_two.text)

    result = first_number + second_number
    print(result)

    browser.find_element(By.TAG_NAME, "select").click()


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()






finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(300)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
