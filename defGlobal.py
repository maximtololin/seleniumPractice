from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Firefox()
def open_link_Firefox(link):
    browser.get(link)
    return browser


# Функция для упрощения наъхождения и вставки значения элемента
def handle_input(type, element, values):
    input_answer = browser.find_element(type, element)
    input_answer.send_keys(values)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def handle_click(type, element):
    browser.find_element(type, element).click()

def handle_submit_result(value_type, value_element, input_type, input_element):
    value_element = browser.find_element(value_type, value_element)

    number_value_element = int(value_element.text)
    result = calc(number_value_element)

    handle_input(input_type, input_element, result)

