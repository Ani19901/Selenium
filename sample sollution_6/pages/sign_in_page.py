import time

from selenium.webdriver.common.by import By

from lib import helpers
from lib.test_logger import logger
from pages.practice_page import click_sign_in_btn
from testdata import test_data

txt_email = (By.ID, "email")
txt_pass = (By.ID, "password")
btn_login = (By.XPATH, "//input[@value='Login']")
msg_invalid = (By.XPATH, "//input[@id='email']//following::span[contains(text(),'invalid')]")


def sign_in():
    click_sign_in_btn()
    helpers.find_and_send_keys(txt_email, test_data.email_data)
    helpers.find_and_send_keys(txt_pass, test_data.pass_data)
    time.sleep(5)
    helpers.find_and_click(btn_login)
    validation_msg = helpers.find(msg_invalid, 60, get_text=True)
    logger(f'Validation Message is - {validation_msg}')
