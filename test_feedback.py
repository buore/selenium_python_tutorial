import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from utilibox import Toolbox


class TestFeedback(Toolbox):
    def test_feedback_fields(self):
        self.url()
        self.navigate_to_feedback_page()
        self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys('testname')
        self.driver.find_element(By.CSS_SELECTOR, "#email").send_keys('test@email.com')
        self.driver.find_element(By.CSS_SELECTOR, "#subject").send_keys('testsomesubjecttext')
        self.driver.find_element(By.CSS_SELECTOR, "#comment").send_keys('testcomments')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='submit']").click()
        feedback = self.driver.find_element(By.CSS_SELECTOR, "#feedback-title").text
        assert feedback == 'Feedback'

