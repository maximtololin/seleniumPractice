from selenium import webdriver
from selenium.webdriver.common.by import By
from config import link_14
from defGlobal import handle_click

browser = webdriver.Firefox()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get(link_14)

handle_click(By.ID, "verify")
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text