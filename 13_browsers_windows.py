import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from defGlobal import open_link_Firefox, handle_submit_result, handle_click


page_link = "http://suninjuly.github.io/redirect_accept.html"



def startUp():
    browser = open_link_Firefox(page_link)
    handle_click(By.CSS_SELECTOR, "[type='submit']")
    # Выбираем второе окно браузера 0,1,2...
    new_window = browser.window_handles[1]
    # Активируем окно
    browser.switch_to.window(new_window)

    time.sleep(3)
    handle_submit_result(By.ID, 'input_value', By.CSS_SELECTOR, "[type='text']" )
    # input_answer = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    # input_answer.send_keys(y)
    handle_click(By.CSS_SELECTOR, "[type='submit']")
    # Принтим алерт на экран
    time.sleep(10)
    print(browser.switch_to.alert.text)
    browser.quit()
startUp()
