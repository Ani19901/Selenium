
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging

driver = None
elements_count = 0
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://courses.letskodeit.com/practice")

# locatotrs via CSS
iframe = (By.ID, "courses-iframe")



# setup logging
logging.basicConfig(filename="log.file",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')


def navigate_iframe():
    driver.switch_to.frame("courses-iframe")
    driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
    time.sleep(5)


if driver:
    driver.quit()
logging.info(f"Found overall {elements_count}!")