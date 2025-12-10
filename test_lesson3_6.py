import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Список ссылок для задания
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)

    # === БЛОК АВТОРИЗАЦИИ ===
    # Так как фикстура browser у тебя scope="function", браузер перезапускается для каждой ссылки.
    # Значит, логиниться нужно каждый раз заново.

    # 1. Ждем и кликаем кнопку входа
    login_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    login_btn.click()

    # 2. Вводим Email
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
    )
    email_input.send_keys("TVOI_EMAIL@GMAIL.COM")  # <--- ВСТАВЬ СВОЙ ЛОГИН

    # 3. Вводим Пароль
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys("TVOI_PAROL")  # <--- ВСТАВЬ СВОЙ ПАРОЛЬ

    # 4. Нажимаем кнопку "Войти"
    submit_btn = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    submit_btn.click()

    # === БЛОК РЕШЕНИЯ ===

    # 5. Ждем, пока загрузится поле для ответа (это значит, что мы залогинились и страница прогрузилась)
    textarea = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea"))
    )

    # 6. Считаем математику
    answer = math.log(int(time.time()))

    # 7. Вводим ответ
    textarea.clear()  # На всякий случай чистим поле
    textarea.send_keys(str(answer))

    # 8. Нажимаем кнопку отправки решения
    # Селектор ищем по классу submit-submission
    solve_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    solve_btn.click()

    # 9. Ждем фидбек (появится сообщение)
    feedback_elt = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    feedback_text = feedback_elt.text

    # 10. Проверяем, что текст совпадает с "Correct!"
    # Если текст БУДЕТ ДРУГОЙ, тест упадет, и в ошибке ты увидишь часть послания инопланетян
    assert feedback_text == "Correct!", f"Инопланетное послание: {feedback_text}"