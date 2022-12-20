from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Firefox()
    browser.get(link)




    input1 = browser.find_element(By.NAME, 'firstname')
    print(input1)
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, 'lastname')
    print(input2)
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, 'e-mail')
    print(input3)
    input3.send_keys("xx@xx.com")

    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys("Lolly")

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла