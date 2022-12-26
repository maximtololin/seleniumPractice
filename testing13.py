import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from defGlobal import open_link_Firefox, handle_input


page_link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def startUp():
    browser = open_link_Firefox(page_link)
    push_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    push_button.click()
    # Выбираем второе окно браузера 0,1,2...
    new_window = browser.window_handles[1]
    # Активируем окно
    browser.switch_to.window(new_window)
    time.sleep(3)
    x_element = browser.find_element(By.ID, 'input_value')
    new_x_element = int(x_element.text)
    x = new_x_element
    y = calc(x)
    handle_input(By.CSS_SELECTOR, "[type='text']", y)
    # input_answer = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    # input_answer.send_keys(y)
    push_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    push_submit.click()
    # Принтим алерт на экран
    time.sleep(10)
    print(browser.switch_to.alert.text)
    browser.quit()
startUp()
