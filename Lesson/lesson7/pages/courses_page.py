from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Courses:

    #Locators
    field_search = (By.XPATH, "//*[@placeholder='Search Course']")
    search_result = (By.XPATH, "//*[@id='course-list']/div")

    # first_result_amount = (By.XPATH, "//*[@id='course-list']/div[1]//span[2]")
    # second_result_amount = (By.XPATH, "//*[@id='course-list']/div[2]//span[2]")
    # third_result_amount = (By.XPATH, "//*[@id='course-list']/div[3]//span[2]")
    btn_sign_in = (By.XPATH, "//*[@id='navbar-inverse-collapse']/div")

    result_amounts = (By.XPATH, "//*[@id='course-list']/div//span[2]")


    def __init__(self, driver):
        self.driver = driver


    def fill_in_search_field(self, search_text):
        self.driver.find_element(*self.field_search).send_keys(search_text)
        self.driver.find_element(*self.field_search).send_keys(Keys.ENTER)

    def get_search_result_count(self):
        return len(self.driver.find_elements(*self.search_result))


    def get_search_result_amount(self):
        list = self.driver.find_elements(*self.result_amounts)
        a =[]
        for i in list:
            a.append(i.text)
        return a





    def click_sign_in_button(self):
        self.driver.find_element(*self.btn_sign_in).click()



