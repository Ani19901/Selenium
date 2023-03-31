from selenium.webdriver.common.by import By
from Helpers import test_logger
from configurations import configs
from Helpers import helpers

input_email = (By.XPATH, "//*[@id='ap_email']")
input_password = (By.XPATH, "//*[@id='ap_password']")
btn_sign_in = (By.XPATH, "//*[@id='signInSubmit']")
msg_validation = (By.XPATH, "//*[contains(text(), 'You are logged ')]")


def login(email, password):
    helpers.find_and_send_keys(input_email, email)
    helpers.find_and_send_keys(input_password, password)
    helpers.find_and_click(btn_sign_in)
    validation_msg = helpers.find(msg_validation, 60, get_text=True)
    test_logger.logger(f'Validation Message is - {validation_msg}')




