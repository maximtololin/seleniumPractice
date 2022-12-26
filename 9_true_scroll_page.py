import time
from selenium.webdriver.common.by import By
from defGlobal import open_link_Firefox
from config import link_9

try:
    browser = open_link_Firefox(link_9)

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("window.scrollBy(0, 100);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(30)
    browser.quit()
