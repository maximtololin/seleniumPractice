import time
from os import getenv
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import stepik_link
from defGlobal import open_link_Firefox, handle_input, handle_click
from dotenv import load_dotenv
import pytest

load_dotenv()
EMAIL = getenv('AUTH__EMAIL')  # получаем из .env секретные переменные, которые не пушатся в git
PASSWORD = getenv('AUTH__PASSWORD')


class TestMainPage1:
    @pytest.mark.smoke
    def test_setup(self):
        self.browser = open_link_Firefox(stepik_link)
        time.sleep(3)
        handle_click(By.ID, "ember33")
        handle_input(By.ID, "id_login_email", str(EMAIL))
        handle_input(By.ID, "id_login_password", str(PASSWORD))
        handle_click(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")

        self.browser.quit()
