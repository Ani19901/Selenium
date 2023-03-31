from selenium.webdriver.common.by import By
from lib import helpers
from testdata import test_data

txt_email = (By.XPATH, "//input[@id='email']")
txt_pass = (By.XPATH, "//input[@id='passwd']")
btn_login = (By.XPATH, "//button[@id='SubmitLogin']")


def sign_in():
    helpers.find_and_send_keys(txt_email, test_data.existing_username)
    helpers.find_and_send_keys(txt_pass, test_data.existing_password)
    helpers.find_and_click(btn_login)
