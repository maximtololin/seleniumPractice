import time
from selenium.webdriver.common.by import By
from defGlobal import open_link_Firefox, handle_click, handle_submit_result
from config import link_12

try:

    browser = open_link_Firefox(link_12)
    handle_click(By.CSS_SELECTOR, "[type='submit']")
    # Переключаемся на алерт
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    handle_submit_result(By.ID, 'input_value', By.CSS_SELECTOR, "[type='text']")
    handle_click(By.CSS_SELECTOR, "[type='submit']")
finally:
    # Принтим алерт на экран
    time.sleep(1)
    print(browser.switch_to.alert.text)
    browser.quit()