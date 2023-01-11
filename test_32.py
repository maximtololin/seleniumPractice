import time
import math
from os import getenv
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from defGlobal import open_link_Firefox, handle_input, handle_click
from dotenv import load_dotenv
import pytest

load_dotenv()
EMAIL = getenv('AUTH__EMAIL')  # получаем из .env секретные переменные, которые не пушатся в git
PASSWORD = getenv('AUTH__PASSWORD')
link = 'https://stepik.org/lesson/236895/step/1'


def calc():
    return str(math.log(int(time.time())))


class TestMainPage1:
    @pytest.mark.smoke
    def test_setup_2(self):
        self.browser = open_link_Firefox(link)
        self.browser.implicitly_wait(10)

        handle_click(By.ID, "ember33")
        handle_input(By.ID, "id_login_email", str(EMAIL))
        handle_input(By.ID, "id_login_password", str(PASSWORD))
        handle_click(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
        time.sleep(10)

        handle_input(By.TAG_NAME, "textarea", calc())
        # WebDriverWait(self.browser, 12).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        # handle_click(By.CSS_SELECTOR, ".submit-submission")

        # WebDriverWait(self.browser, 12).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        # WebDriverWait(self.browser, 12).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        # print(new_answer)
        # # correct_answer = new_answer
        # #
        # # assert "Correct!" == correct_answer

        self.browser.quit()
