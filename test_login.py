
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
from .utilibox import Toolbox


class Testlogin(Toolbox):
    load_dotenv()
    secret_username = os.getenv('UNAME')
    secret_password = os.getenv('PASSWD')
    invalid_password = os.getenv('INVALID_PASSWD')

    def test_url(self):
        self.driver.get(os.getenv('BASE_URL'))
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.getenv('BASE_URL') in page_url

    def test_login_with_valid_creds(self):
        self.login(self.secret_username, self.secret_password)

        self.driver.back()

        assert self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[1].text == self.secret_username

        self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[1].click()

        self.driver.find_element(By.CSS_SELECTOR, '#logout_link').click()

    def test_login_with_invalid_creds(self):
        self.login(self.secret_username, self.invalid_password)
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-error").text == "Login and/or password are wrong."


