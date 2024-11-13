from selenium.common.exceptions import NoSuchElementException
import time

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_notepad_index():

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # Initialise the browser using WebDriver Manager
    # service = Service(ChromeDriverManager().install())
    
    driver = initialize_driver()
    try:
        host = get_host_for_selenium_testing()

        # Open the index page
        driver.get(f'{host}/notepad')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        try:

            pass

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)
        print("test passed!")


# Call the test function
test_notepad_index()
