from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
def open_link_Firefox(link):
    browser.get(link)
    return browser


# Функция для упрощения наъхождения и вставки значения элемента
def handle_input(type, element, values):
    input_answer = browser.find_element(type, element)
    input_answer.send_keys(values)

