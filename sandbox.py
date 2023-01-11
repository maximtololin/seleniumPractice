from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from defGlobal import handle_click, open_link_Firefox


link = "https://ok.ru/"

def startUp():
    browser = open_link_Firefox(link)
    browser.implicitly_wait(5)
    # time.sleep(10)
    handle_click(By.CSS_SELECTOR, '.button-pro.__wide[data-l="t,sign_in"]')
    print("Im found button")
    # message = browser.find_element(By.ID, "verify_message")
    #
    # assert "successful" in message.text

    browser.quit()

startUp()
