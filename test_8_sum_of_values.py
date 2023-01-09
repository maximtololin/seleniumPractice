from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from defGlobal import open_link_Firefox, handle_click
from config import link_8

# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"

# Можно использовать еще два метода: select.select_by_visible_text("text") и
# select.select_by_index(index). Первый способ ищет элемент по видимому тексту,
# например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.
#
# Второй способ ищет элемент по его индексу или порядковому номеру.
# Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python",
# нужно использовать select.select_by_index(1), так как опция с индексом 0 в
# данном примере имеет значение по умолчанию равное "--".


def sum(x, y):
    return str(x + y)


try:
    browser = open_link_Firefox(link_8)

    new_el1 = browser.find_element(By.ID, 'num1')
    first_number = int(new_el1.text)
    new_el2 = browser.find_element(By.ID, 'num2')
    second_number = int(new_el2.text)

    total_sum = sum(first_number, second_number)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total_sum)

    handle_click(By.TAG_NAME, 'button')

finally:
    time.sleep(30)
    browser.quit()