from selenium.webdriver.common.by import By
from lib import helpers
from lib.test_logger import logger
from testdata import test_data


btn_contact_us = (By.XPATH,'.//*[@title ="Contact Us"]')
input_email = (By.XPATH,'.//*[@id="email"]')
input_order = (By.XPATH,'.//*[@id="id_order"]')
file_choose = (By.XPATH,'.//*[@id="fileUpload"]')
msg_input = (By.XPATH,'.//*[@id="message"]')
btn_submit = (By.XPATH,'.//*[@id="submitMessage"]')
msg_invalid = (By.XPATH,'.//*[@class="alert alert-danger"]')


def check_contact_us_negative():
    helpers.find_and_click(btn_contact_us)
    helpers.find_and_click(btn_submit)
    validation_msg = helpers.find(msg_invalid, 60, get_text=True)
    logger(f'Validation Message is - {validation_msg}')


def check_contact_us_positive():
    helpers.find_and_click(btn_contact_us)
    helpers.find_and_send_keys(input_email, "mail.ru")
    helpers.find_and_send_keys(input_order, "my_tttt")
    helpers.find_and_click(btn_submit)





