# # Файл для использования быстрыго вызова фикстур.
# # Такой файл необходимо использовать либо в проекте, либо в блоке тестов.
# # Вот так:
# #
# # selenium_course_solutions/
# # ├── section3
# # │   └── conftest.py
# # │   └── test_languages.py
# # ├── section4
# # │   └── conftest.py
# # │   └── test_main_page.py
# #
# # правильно!
#
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Фикстура для использования браузера в разных тестах
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Firefox()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()