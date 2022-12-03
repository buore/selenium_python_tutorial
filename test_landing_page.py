import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from .utilibox import Toolbox


class TestLandingPage(Toolbox):
    def take_scrn_shot(self):
        self.driver.save_screenshot(f"screenshots/{datetime.datetime.now()}-image.png")

    def test_landing_page(self):
        self.url()
        landing_page_text = self.driver.find_element(By.CSS_SELECTOR, ".brand").text
        assert landing_page_text == 'Zero Bank', self.take_scrn_shot()

    def test_searchbox(self):
        search_box=self.driver.find_element(By.CSS_SELECTOR, "#searchTerm")
        search_box.send_keys('faketest')
        search_box.send_keys(Keys.ENTER)
        assert self.driver.find_element(By.CSS_SELECTOR, ".top_offset > h2").text == 'Search Results:'
        self.home()

    def test_home_page_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, "#homeMenu").click()
        self.driver.find_element(By.CSS_SELECTOR, "#onlineBankingMenu").click()
        self.driver.find_element(By.CSS_SELECTOR, "#feedback").click()


