from selenium.webdriver.common.by import By
from Helpers import helpers
from Helpers import test_logger
from configurations import configs

icon_login = (By.XPATH, ".//*[@class='y-z']")
btn_accessories = (By.XPATH, './/*[@href ="/accessories"]')
link_watches = (By.XPATH, "//*[@data-eventvalue='A-TOPCAT-WomensWatches']")


def login_page_navigation():  
    test_logger.logger('Opening websites home page')
    helpers.find_and_click(icon_login)
    test_logger.logger("Trying to click login")

