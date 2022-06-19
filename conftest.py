from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(autouse=True, scope='class')
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    request.cls.driver = driver

    yield

    driver.quit()
