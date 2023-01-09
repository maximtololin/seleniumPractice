from selenium.webdriver.common.by import By
import time
from defGlobal import open_link_Firefox, handle_click, handle_input, calc, handle_submit_result
from config import link_7

def handle_calc_result(value_type, value_element, input_type, input_element, attr):
    value_element = browser.find_element(value_type, value_element).get_attribute(attr)

    number_value_element = int(value_element)
    result = calc(number_value_element)

    handle_input(input_type, input_element, result)

try:
    browser = open_link_Firefox(link_7)

    handle_calc_result(By.ID, 'treasure', By.ID, 'answer', 'valuex')

    handle_click(By.ID, 'robotCheckbox')
    handle_click(By.ID, 'robotsRule')
    handle_click(By.CSS_SELECTOR, 'button.btn')

finally:
    time.sleep(30)
    browser.quit()