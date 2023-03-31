from selenium.webdriver.common.by import By


class Login:

    btn_sign_in = (By.XPATH, "//a[text()='Sign In']")
    field_email = (By.XPATH, "//*[@id='page']//form/div[1]/input")
    field_password = (By.XPATH, "//*[@id='password']")
    btn_login = (By.XPATH, "//*[@id='page']//form/div[4]//input")
    txt_message = (By.XPATH, "//*[@id='page']//form/div[1]/span")

    def __init__(self, driver):
        self.driver = driver


    def click_sign_in_button(self):
        self.driver.find_element(*self.btn_sign_in).click()


    def fill_in_email_field(self, email_text):
        self.driver.find_element(*self.field_email).send_keys(email_text)

    def fill_in_password_field(self, password_text):
        self.driver.find_element(*self.field_password).send_keys(password_text)

    def click_login_btn(self):
        self.driver.find_element(*self.btn_login).click()

    def get_invalid_message_text(self):
        return self.driver.find_element(*self.txt_message).text

