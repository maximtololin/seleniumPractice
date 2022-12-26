import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)
    push_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    push_button.click()
    # Переключаемся на алерт
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    x_element = browser.find_element(By.ID, 'input_value')
    new_x_element = int(x_element.text)
    x = new_x_element
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    input_answer.send_keys(y)
    push_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    push_submit.click()
finally:
    # Принтим алерт на экран
    time.sleep(1)
    print(browser.switch_to.alert.text)
    browser.quit()