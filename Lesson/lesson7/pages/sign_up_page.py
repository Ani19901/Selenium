from selenium.webdriver.common.by import By


class SignUP:

    #Locators
    first_name = (By.XPATH, "//*[@id='name']")
    last_name = (By.XPATH, "//*[@id='last_name']")
    email_field = (By.XPATH, "//*[@id='email']")
    password_field = (By.XPATH, "//*[@id='password']")
    confirm_password_field = (By.XPATH, "//*[@id='password_confirmation']")
    btn_sign_up = (By.XPATH, "//input[@value = 'Sign Up']")

    def __init__(self, driver):
        self.driver = driver


    def fill_in_input_fields(self, first_name_text, last_name_text, email_text, password_text):
        self.driver.find_element(*self.first_name).send_keys(first_name_text)
        self.driver.find_element(*self.last_name).send_keys(last_name_text)
        self.driver.find_element(*self.email_field).send_keys(email_text)
        self.driver.find_element(*self.password_field).send_keys(password_text)
        self.driver.find_element(*self.confirm_password_field).send_keys(password_text)


    def click_sign_up_button(self):
        self.driver.find_element(*self.btn_sign_up).click()
