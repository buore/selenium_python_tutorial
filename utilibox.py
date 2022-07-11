import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By


class Toolbox:
    load_dotenv()
    secret_username = os.environ['UNAME']
    secret_password = os.environ['PASSWD']
    invalid_password = os.environ['INVALID_PASSWD']

    def url(self):
        self.driver.get(os.environ['BASE_URL'])
        self.driver.maximize_window()
        page_url = self.driver.current_url
        assert os.environ['BASE_URL'] in page_url

    def login(self, uname, pword):
        self.driver.find_element(By.CSS_SELECTOR, '#signin_button').click()
        self.driver.find_element(By.CSS_SELECTOR, "#user_login").send_keys(uname)
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys(pword)
        self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="Sign in"]').click()
