from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from defGlobal import open_link_Firefox, handle_input, handle_click
from config import link_3


try:
    browser = open_link_Firefox(link_3)

    handle_input(By.NAME, 'first_name', "Ivan")
    handle_input(By.NAME, 'last_name', "Petrov")
    handle_input(By.NAME, 'e-mail', "xx@xx.com")

    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys("Lolly")

    handle_click(By.CSS_SELECTOR, 'button.btn')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла