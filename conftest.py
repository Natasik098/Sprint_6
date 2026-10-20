import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    service = Service(executable_path="drivers/geckodriver.exe")

    options = webdriver.FirefoxOptions()
    options.binary_location = r"C:\Firefox\Firefox\firefox.exe"

    driver = webdriver.Firefox(
        service=service,
        options=options
    )
    
    driver.maximize_window()

    yield driver

    driver.quit()