import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# Во время выполнения 1 теста, открывается 2 окна браузера с помощью фикстуры.
# Был создан метод browser. Так же указали что он является фикстурой за счет декоратора

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()

    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")