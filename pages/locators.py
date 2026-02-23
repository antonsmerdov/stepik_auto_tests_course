from selenium.webdriver.common.by import By

class MainPageLocators():
    # Локатор для ссылки на главной странице
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    # Локаторы для форм на странице логина
    # Обрати внимание на названия, они должны совпадать с тем, что ты импортируешь
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
