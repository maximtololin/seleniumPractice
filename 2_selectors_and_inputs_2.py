from selenium.webdriver.common.by import By
import time
from defGlobal import open_link_Firefox, handle_input, handle_click
from config import link_2


try:
    browser = open_link_Firefox(link_2)

    handle_click(By.PARTIAL_LINK_TEXT, "224592")

    handle_input(By.NAME, 'first_name', "Ivan")
    handle_input(By.NAME, 'last_name', "Petrov")
    handle_input(By.CLASS_NAME, 'city', "Smolensk")
    handle_input(By.ID, 'country', "Russia")

    handle_click(By.CSS_SELECTOR, 'button.btn')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла