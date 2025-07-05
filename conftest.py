import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture
def driver():
    chromedriver_path = "D:/QAautomatizacion/chromedriver.exe"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
