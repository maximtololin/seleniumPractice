from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from defGlobal import open_link_Firefox, handle_click, handle_submit_result



page_link = "http://suninjuly.github.io/explicit_wait2.html"



def startUp():
    browser = open_link_Firefox(page_link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    handle_click(By.ID, 'book')

    handle_submit_result(By.ID, 'input_value', By.ID, 'answer')

    handle_click(By.ID, 'solve')
    time.sleep(10)
    print(browser.switch_to.alert.text)
    browser.quit()

startUp()