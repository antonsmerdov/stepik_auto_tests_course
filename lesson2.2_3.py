from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.NAME, "firstname")
    input_first_name.send_keys("Gleb")

    input_last_name = browser.find_element(By.NAME, "lastname")
    input_last_name.send_keys("Severov")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("supertest@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, "../stepik/test.txt")  # добавляем к этому пути имя файла

    browser.find_element(By.ID, "file").send_keys(file_path)


    button_submit = browser.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3000)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
