from selenium.webdriver.common.by import By

class MainPageLocators():
    # Локатор для ссылки на главной странице
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # Локаторы для форм на странице логина
    # Обрати внимание на названия, они должны совпадать с тем, что ты импортируешь
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")