from selenium.webdriver.common.by import By
from final_assessment.Helpers import helpers, log
from final_assessment.TestData import testdata

inp_first_name_field = (By.XPATH, "//*[@id = 'user[first_name]']")
inp_last_name_field = (By.XPATH, "//*[@id = 'user[last_name]']")
inp_email_field = (By.XPATH, "//*[@id = 'user[email]']")
inp_password_field = (By.XPATH, "//*[@id = 'user[password]']")
checkbox_terms = (By.XPATH, "//*[@id ='user[terms]']")
btn_sign_up = (By.XPATH, "//input[ @value = 'Sign up']")


def registration(driver):
    try:
        helpers.find_and_send_keys(driver, inp_first_name_field, testdata.first_name)
        helpers.find_and_send_keys(driver, inp_last_name_field, testdata.last_name)
        helpers.find_and_send_keys(driver, inp_email_field, testdata.email)
        helpers.find_and_send_keys(driver, inp_password_field, testdata.password)
        helpers.find_and_click(driver, checkbox_terms)
        helpers.update_json(testdata.email, testdata.password)
        helpers.find_and_click(driver, btn_sign_up)
        log.logger("The system is sign up")
    except Exception as e:
        log.logger(e)