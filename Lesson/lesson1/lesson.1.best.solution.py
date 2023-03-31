from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging


# Keep browsers in list
drivers = ["chrome", "firefox", "edge"]

# setup logging
log_format = "%(asctime)s: - %(levelname)s:%(message)s"
logging.basicConfig(filename="log_file.txt", encoding='utf-8', format=log_format, level=logging.INFO)


def my_test(driver):
    driver.maximize_window()
    driver.get("https://python.org")
    search = driver.find_element_by_id("id-search-field")
    go_button = driver.find_element_by_id("submit")
    search.send_keys("bla-bla")
    go_button.click()
    assert driver.find_elements_by_xpath("//p[text()='No results found.']"), "Failed"
    driver.close()


def get_driver(driver_name):
    if driver_name is "chrome":
        return webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif driver_name is "firefox":
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif driver_name is "edge":
        return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        logging.error(f"Driver '{driver_name}' not found!!")


for browser in drivers:
    logging.info(f"-> Run test with {browser} browser")
    driver = get_driver(browser)
    try:
        my_test(driver)
        logging.info("<- Success")
    except Exception as e:
        logging.error(e)

    finally:
        if driver:
            driver.quit()