import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    new_x_element = int(x_element.text)
    print(new_x_element)
    x = new_x_element
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    activate_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    activate_checkbox.click()
    activate_radiobutton = browser.find_element(By.ID, 'robotsRule')
    activate_radiobutton.click()
    push_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    push_submit.click()
finally:
    time.sleep(30)
    browser.quit()