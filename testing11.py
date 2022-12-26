import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("Lol")
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys("Kek")
    email_name = browser.find_element(By.NAME, 'email')
    email_name.send_keys("cheburek@kek.com")
    # Переменная с директорией текущего файла, для добавления следующего
    current_dir = os.path.abspath(os.path.dirname("testing11.py"))
    # Указываем файл для загрузки
    file_name = "loading_sample.txt"
    # Получаем путь файла для загрузки
    file_path = os.path.join(current_dir, "loading_sample.txt")
    # Находим эелемент загрузки на странице по селектору
    download_element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # Загружаем файл с помощью элемента и указываем путь к файлу
    download_element.send_keys(file_path)
    push_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    push_submit.click()
finally:
    time.sleep(30)
    browser.quit()


