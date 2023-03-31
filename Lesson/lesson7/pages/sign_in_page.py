from selenium.webdriver.common.by import By


class SignIn:

    #Locators
    btn_sign_up = (By.XPATH, "//a[text() = ' Sign Up']")
    email_field = (By.XPATH, "//*[@id='email']")
    password_field = (By.XPATH, "//*[@id='password']")
    btn_login = (By.XPATH, "//*[@value = 'Login']")

    png_user_profile = (By.XPATH, "//*[@id='dropdownMenu1']/img")
    btn_log_out = (By.XPATH, "//a[text() = 'Logout']")


    def __init__(self, driver):
        self.driver = driver

    def click_sign_up_button(self):
        self.driver.find_element(*self.btn_sign_up).click()

    def fill_in_input_fields(self, email_text, password_text):
        self.driver.find_element(*self.email_field).send_keys(email_text)
        self.driver.find_element(*self.password_field).send_keys(password_text)

    def click_login_button(self):
        self.driver.find_element(*self.btn_login).click()


    def user_profile_png_is_displayed(self):
        return self.driver.find_element(*self.png_user_profile).is_displayed()


    def log_out(self):
        self.driver.find_element(*self.png_user_profile).click()
        self.driver.find_element(*self.btn_log_out).click()



