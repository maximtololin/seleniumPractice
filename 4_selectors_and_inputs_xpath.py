from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Firefox()
    browser.get(link)




    input1 = browser.find_element(By.NAME, 'first_name')
    print(input1)
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, 'last_name')
    print(input2)
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, 'city')
    print(input3)
    input3.send_keys("Erevan")

    input4 = browser.find_element(By.ID, 'country')
    print(input4)
    input4.send_keys("Armenia")

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    time.sleep(10)

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


