from selenium.webdriver.common.by import By

# --- БАЗОВЫЕ ЛОКАТОРЫ (ДЛЯ ВСЕХ СТРАНИЦ) ---
class BasePageLocators():
    # Ссылки в шапке сайта, которые есть везде
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group > a") # Кнопка корзины

# --- ЛОКАТОРЫ ГЛАВНОЙ СТРАНИЦЫ ---
class MainPageLocators():
    # Пока оставляем пустым (pass означает "пропустить"),
    # так как ссылку на логин мы вынесли в BasePageLocators
    pass

# --- ЛОКАТОРЫ СТРАНИЦЫ КОРЗИНЫ ---
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items") # Блок со списком товаров
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p") # Текст "Your basket is empty"

# --- ЛОКАТОРЫ СТРАНИЦЫ ЛОГИНА ---
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    # Вот эти локаторы для регистрации нужно добавить:
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button[type='submit']")

# --- ЛОКАТОРЫ СТРАНИЦЫ ТОВАРА ---
class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasePageLocators():
    # ... твои старые локаторы ...
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") # Добавили по заданию