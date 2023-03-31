from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging
import time


logging.basicConfig(filename="../log.information", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')


def test(driver):
    driver.get("https://www.python.org/")
    driver.maximize_window()
    search_field = driver.find_element_by_xpath("//*[@id='id-search-field']")
    search_field.clear()
    search_field.send_keys("loo")
    driver.find_element_by_id("submit").click()
    assert "No results found."
    logging.info("The assertion is passed")
    time.sleep(3)
    driver.close()


drivers = ['ChromeDriver', 'GeckoDriver', 'EdgeDriver']

try:
    for i in drivers:
        if i == 'ChromeDriver':
            driver = webdriver.Chrome(ChromeDriverManager().install())
            test(driver)
            logging.info("Test for the " + i)

        elif i == 'GeckoDriver':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            test(driver)
            logging.info('Test for the ' + i)

        elif i == 'EdgeDriver':
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            test(driver)
            logging.info('Test for the ' + i)

except Exception as x:
    logging.error(f"Validation is failed \n {x}")
    exit(1)


