from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Firefox()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, 'treasure')
    x_element_check = x_element.get_attribute('valuex')
    print(x_element_check)
    x = x_element_check
    y = calc(x)
    print(y)

    input1 = browser.find_element(By.ID, 'answer')
    print(input1)
    input1.send_keys(y)

    activate_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    activate_checkbox.click()

    activate_radiobutton = browser.find_element(By.ID, 'robotsRule')
    activate_radiobutton.click()

    push_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    push_submit.click()


finally:
    time.sleep(30)
    browser.quit()