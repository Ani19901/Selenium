import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = None
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.uitestingplayground.com/home")


# locators
class_attribute = (By.XPATH, "//a[contains(text(),'Class Attribute')]")
btns = (By.XPATH,  "//button[contains(@class, 'btn')]")


# logging.basicConfig(filename="../log.file",
#                     level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filemode='w')




def click_class_attribute():
    driver.find_element(*class_attribute).click()


def get_btn_value():
    items = driver.find_elements(*btns)
    for i in items:
        print(i.get_attribute("class"))


def my_test():
    click_class_attribute()
    get_btn_value()


my_test()


if driver:
    driver.quit()
