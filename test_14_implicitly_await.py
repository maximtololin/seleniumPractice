import time

from selenium.webdriver.common.by import By
from config import link_14
from defGlobal import handle_click, open_link_Firefox
import pytest


class TestMe:
    @pytest.mark.smoke
    def test_setUp(self):
        browser = open_link_Firefox(link_14)
        browser.implicitly_wait(5)
        # говорим WebDriver искать каждый элемент в течение 5 секунд
        handle_click(By.ID, "verify")
        message = browser.find_element(By.ID, "verify_message")

        assert "successful" in message.text

        browser.quit()



