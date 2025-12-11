import time  # <--- ОШИБКА 1: Был неправильный импорт
from selenium import webdriver

# Строка ниже не нужна, если мы создаем драйвер вручную
# from stepik.autostet import browser

# Инициализируем драйвер
browser = webdriver.Firefox()

browser.get("https://stepik.org/lesson/25969/step/8")

time.sleep(3)

# <--- ОШИБКА 2: Переменная называется driver, а не browser
browser.quit()