from selenium.webdriver.common.by import By
from Helpers import helpers
from configurations import configs

input_email = (By.XPATH, "//*[@id='ap_email']")
input_password = (By.XPATH, "//*[@id='ap_passwordl']")
btn_sign_in = (By.XPATH,"//*[@id='signInSubmit']")
msg_validation = (By.XPATH, "//*[contains(text(), 'You are logged ')]")


def login(email, password):
    helpers.find_and_send_keys(email, configs.email)
    helpers.find_and_send_keys(password, configs.password)
    helpers.find_and_click(btn_sign_in)
    validation_msg = helpers.find(msg_validation, 60, get_text=True)
    #test_logger.logger(f'Validation Message is - {validation_msg}')




