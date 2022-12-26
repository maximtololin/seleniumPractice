import time
from selenium.webdriver.common.by import By
import os
from defGlobal import open_link_Firefox, handle_click, handle_input
from config import link_11

try:
    browser = open_link_Firefox(link_11)

    handle_input(By.NAME, 'firstname', "Lol")
    handle_input(By.NAME, 'lastname', "Kek")
    handle_input(By.NAME, 'email', "cheburek@kek.com")

    # Переменная с директорией текущего файла, для добавления следующего
    current_dir = os.path.abspath(os.path.dirname("11_download_file.py"))
    # Указываем файл для загрузки
    file_name = "loading_sample.txt"
    # Получаем путь файла для загрузки
    file_path = os.path.join(current_dir, file_name)
    # Находим эелемент загрузки на странице по селектору
    download_element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # Загружаем файл с помощью элемента и указываем путь к файлу
    download_element.send_keys(file_path)
    handle_click(By.CSS_SELECTOR, "[type='submit']")
finally:
    time.sleep(30)
    browser.quit()


