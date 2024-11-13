from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from core.environment.host import get_host_for_selenium_testing
import os


def initialize_driver():
    # Initializes the browser options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    working_dir = os.getenv('WORKING_DIR', "")

    if working_dir == "/app/":
        host = get_host_for_selenium_testing()
        print(f"{host}:4444/wd/hub")
        driver = webdriver.Remote(
            command_executor="http://172.17.0.1:4444/wd/hub",
            options=options
            )
    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    return driver


def close_driver(driver):
    driver.quit()
