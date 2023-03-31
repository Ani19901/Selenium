from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    try:
        return webdriver.Chrome(ChromeDriverManager().install())
    except Exception as error:
        raise Exception(error)


def back_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())  #TODO duplicate code
    driver.back()