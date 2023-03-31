from selenium.webdriver.common.by import By


class SignUP:

    first_name = (By.XPATH, "//*[@id='name']")
    last_name = (By.XPATH, "//*[@id='last_name']")
    email_field = (By.XPATH, "//*[@id='email']")
    password_field = (By.XPATH, "//*[@id='password']")
    confirm_password_field = (By.XPATH, "//*[@id='password_confirmation']")
    btn_sign_up = (By.XPATH, "//input[@value = 'Sign Up']")

    def __init__(self, driver):
        self.driver = driver


    def fill_in_first_name_field(self, text):
        self.driver.find_element(*self.first_name).send_keys(text)

    def fill_in_last_name_field(self, text):
        self.driver.find_element(*self.last_name).send_keys(text)

    def fill_in_email_field(self, text):
        self.driver.find_element(*self.email_field).send_keys(text)

    def fill_in_password_field(self, text):
        self.driver.find_element(*self.password_field).send_keys(text)

    def fill_in_confirm_password_field(self, text):
        self.driver.find_element(*self.confirm_password_field).send_keys(text)

    def click_sign_up_button(self):
        self.driver.find_element(*self.btn_sign_up).click()

