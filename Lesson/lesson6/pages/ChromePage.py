from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Lesson.lesson6.helper.helper_driver import webdriver


driver1 = driver
class ChromePage:

    input_google_search = (By.XPATH, ".//*[@role='search']//div/div/input")
    search_result_text = (By.XPATH, "//*[@id='result-stats']")

    # def __init__(self, driver):
    #     self.driver = driver

    def fill_in_search_field(self, text):
        self.driver1.find_element(*self.input_google_search).send_keys(text)
        self.driver1.find_element(*self.input_google_search).send_keys(Keys.RETURN)

    def get_result_count(self):
        return self.driver1.find_element(*self.search_result_text).text


    driver1.setup
