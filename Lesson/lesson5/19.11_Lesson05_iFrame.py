import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://courses.letskodeit.com/practice")
#driver.implicitly_wait(10)


#locatotrs
btn_sign_in = (By.XPATH, "//a[text()='Sign In']")



#setup logging
logging.basicConfig(filename="log.file.iFrame",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')


def click_sign_in_btn():
    driver.find_element(*btn_sign_in).click()


def navigate_iframe():
    driver.switch_to.frame("courses-iframe")
    logging.info(f"Navigate to iFrame Example")
    click_sign_in_btn()
    logging.info(f"Click on 'Sign in' button on the iFrame Example")
    time.sleep(3)
    driver.switch_to.default_content()
    logging.info(f"Navigate to default iFrame")
    click_sign_in_btn()
    time.sleep(3)
    logging.info(f"Click on 'Sign in' button on the default iFrame")


navigate_iframe()

if driver:
    driver.quit()
logging.info(f"The page and iFrame are closed")