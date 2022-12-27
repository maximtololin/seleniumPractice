from selenium.webdriver.common.by import By
import time
from defGlobal import open_link_Firefox, handle_input, handle_click
from config import link_5, link_16
import pytest
import unittest


def test_setUp1():

    browser = open_link_Firefox(link_5)

    handle_input(By.CLASS_NAME, "first", "Kek")
    handle_input(By.CLASS_NAME, "second", "Kek2")
    handle_input(By.CLASS_NAME, "third", "kek@kek.com")
    handle_input(By.XPATH, "//input[@placeholder='Input your phone']", "89999999999")

    handle_click(By.CSS_SELECTOR, "button.btn")

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)
    browser.quit()

    if __name__ == "__main__":
            pytest.main()

def test_setUp2():

    browser = open_link_Firefox(link_16)

    handle_input(By.CLASS_NAME, "first", "Kek")
    handle_input(By.CLASS_NAME, "second", "Kek2")
    handle_input(By.CLASS_NAME, "third", "kek@kek.com")
    handle_input(By.XPATH, "//input[@placeholder='Input your phone']", "89999999999")

    handle_click(By.CSS_SELECTOR, "button.btn")

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)
    browser.quit()

    if __name__ == "__main__":
            pytest.main()

