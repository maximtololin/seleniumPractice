from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from defGlobal import open_link_Firefox, handle_input, handle_click
from config import link_5

try:
    browser = open_link_Firefox(link_5)

    handle_input(By.CLASS_NAME, "first", "Kek")
    handle_input(By.CLASS_NAME, "second", "Kek2")
    handle_input(By.CLASS_NAME, "third", "kek@kek.com")
    handle_input(By.XPATH, "//input[@placeholder='Input your phone']", "89999999999")

    # Отправляем заполненную форму
    handle_click(By.CSS_SELECTOR, "button.btn")

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()