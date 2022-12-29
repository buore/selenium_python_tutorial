from selenium.webdriver.common.by import By
from utilibox import Toolbox


class Testlogin(Toolbox):

    def test_login_with_valid_creds(self):
        self.url()
        self.login(self.secret_username, self.secret_password)
        self.driver.back()
        assert self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[1].text == self.secret_username
        self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[1].click()
        self.driver.find_element(By.CSS_SELECTOR, '#logout_link').click()

    def test_login_with_invalid_creds(self):
        self.login(self.secret_username, self.invalid_password)
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-error").text == "Login and/or password are wrong."