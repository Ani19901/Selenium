from selenium.webdriver.common.by import By
from final_assessment.Helpers import helpers, log
from final_assessment.Pages import sign_up


inp_email_field = (By.XPATH, "//*[@id = 'user[email]']")
inp_password_field = (By.XPATH, "//*[@id = 'user[password]']")
checkbox_remember_me = (By.XPATH, "//*[@id = 'user[remember_me]']")
btn_sign_in = (By.XPATH, "//input[ @value = 'Sign in']")
lnk_create_new_account = (By.XPATH, "//a[contains(text(), 'Create a new account')]")


def login(driver):
    data = helpers.json_data()
    if data["email"] == '' or data["password"] == '':
        helpers.find_and_click(driver, lnk_create_new_account)
        sign_up.registration(driver)
    else:
        helpers.find_and_send_keys(driver, inp_email_field, data["email"])
        helpers.find_and_send_keys(driver, inp_password_field, data["password"])
        helpers.find_and_click(driver, checkbox_remember_me)
        helpers.find_and_click(driver, btn_sign_in)
        log.logger("The system is sign in")