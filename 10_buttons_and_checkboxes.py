import time
from selenium.webdriver.common.by import By
from defGlobal import open_link_Firefox, handle_click, handle_submit_result
from config import link_10

try:
    browser = open_link_Firefox(link_10)

    handle_submit_result(By.ID, 'input_value', By.ID, 'answer')

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    handle_click(By.ID, 'robotCheckbox')
    handle_click(By.ID, 'robotsRule')
    handle_click(By.CSS_SELECTOR, 'button.btn')
finally:
    time.sleep(30)
    browser.quit()
