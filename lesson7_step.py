from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    people_checked = x_element.get_attribute("valuex")
    x = people_checked
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button = browser.find_element(By.ID, "robotsRule")
    button.click()

    # button = browser.find_element(By.ID, "answer")
    # button.click()

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
    print("Браузер закрыт")