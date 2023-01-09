from selenium.webdriver.common.by import By
import time
from defGlobal import open_link_Firefox, handle_click, handle_submit_result
from config import link_6


try:
    browser = open_link_Firefox(link_6)

    handle_submit_result(By.ID, 'input_value', By.ID, 'answer')

    handle_click(By.ID, 'robotCheckbox')
    handle_click(By.ID, 'robotsRule')
    handle_click(By.CSS_SELECTOR, 'button.btn')


finally:
    time.sleep(30)
    browser.quit()

