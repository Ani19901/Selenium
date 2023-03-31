import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
import random

# ==========================================================
# Logging configurations
logging.basicConfig(filename="out.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://www.uitestingplayground.com/")
driver.maximize_window()

# Assignment 02
# ================================================

lst_button_names = []
lnk_mouserover = (By.XPATH, "//*[text()='Mouse Over']")
lnk_click_me = (By.XPATH, "//a[text()='Click me']")
txt_count = (By.ID, "clickCount")


def mouse_over():
    driver.find_element(*lnk_mouserover).click()
    logging.info(f"Click on the {lnk_mouserover} element")
    count = random.randint(1, 17)
    for i in range(0, count):
        driver.find_element(*lnk_click_me).click()

    logging.info(f"Click on the link {count} times")
    time.sleep(3)
    count_from_page = driver.find_element(*txt_count).text
    logging.info(f"The clicks count is {count_from_page}")
    assert (count, int(count_from_page))

try:
    mouse_over()
    driver.close()
except Exception as err:
    logging.error(err)

