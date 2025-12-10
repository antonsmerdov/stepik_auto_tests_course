import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import math

# --- ИМПОРТ ПАРОЛЕЙ ---
try:
    from auth_data import email, password
except ImportError:
    email = None
    password = None

links = [
    "https://stepik.org/lesson/236895/step/1"
]


@pytest.mark.parametrize('link', links)
def test_stepik_alien_message(browser, link):
    print(f"\n[LOG] Открываем ссылку: {link}")
    browser.get(link)

    # === 1. АВТОРИЗАЦИЯ ===
    try:
        login_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
        )
        login_btn.click()

        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
        )
        email_input.send_keys(email)

        browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)

        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()

        # Ждем исчезновения окна логина
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
        )
        print("[LOG] Авторизация успешна.")

    except TimeoutException:
        print("[LOG] Окно входа не найдено, возможно мы уже залогинены.")

    # === 2. ПОДГОТОВКА ===
    try:
        again_btn = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn"))
        )
        again_btn.click()
        print("[LOG] Нажата кнопка 'Решить снова'.")
        time.sleep(1)
    except:
        pass

    # === 3. ВВОД ОТВЕТА ===
    print("[LOG] Ищем поле ввода...")
    textarea = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ember-text-area"))
    )

    answer = math.log(int(time.time()))
    print(f"[LOG] Ответ: {answer}")

    textarea.clear()
    textarea.send_keys(str(answer))

    # ПРОВЕРКА: Реально ли текст попал в поле?
    entered_text = textarea.get_attribute("value")
    print(f"[LOG] Текст в поле сейчас: '{entered_text}'")

    # === 4. ОТПРАВКА (УМНЫЙ КЛИК) ===
    print("[LOG] Ищем кнопку Отправить...")
    solve_btn = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.submit-submission"))
    )

    # Ждем пока кнопка станет активной
    WebDriverWait(browser, 10).until(lambda d: solve_btn.is_enabled())
    time.sleep(1)  # Короткая пауза

    print("[LOG] Пытаемся кликнуть...")

    # Попытка 1: Обычный клик (часто работает лучше, чем JS, если сайт ждет фокуса)
    try:
        solve_btn.click()
        print("[LOG] Сделан обычный клик.")
    except:
        # Попытка 2: Если обычный не прошел (перекрыта), бьем через JS
        print("[LOG] Обычный клик не прошел, используем JS...")
        browser.execute_script("arguments[0].click();", solve_btn)

    # === 5. ПРОВЕРКА РЕЗУЛЬТАТА ===
    print("[LOG] Ждем фидбек...")

    # Ищем ЛЮБОЙ фидбек (Хороший или Плохой)
    # Это поможет понять, нажимается ли кнопка вообще
    try:
        feedback = WebDriverWait(browser, 15).until(
            EC.visibility_of_any_elements_located(
                (By.CSS_SELECTOR, ".smart-hints__hint, .attempt-message_wrong, .attempt-message_correct"))
        )
        # Берем текст первого найденного элемента
        feedback_text = feedback[0].text
        print(f"[LOG] УРА! Получен фидбек: '{feedback_text}'")
    except TimeoutException:
        print("[LOG] ОШИБКА: Фидбек так и не появился за 15 секунд.")
        feedback_text = "No feedback"

    # Финальная проверка
    assert feedback_text == "Correct!", f"Ожидался 'Correct!', а получили: {feedback_text}"