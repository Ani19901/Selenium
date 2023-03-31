from selenium.webdriver.common.by import By


class Practice:


    #Locators
    lnk_all_courses = (By.XPATH, "//a[text() ='ALL COURSES']")
    btn_sign_in = (By.XPATH, "//a[text() ='Sign In']")

    def __init__(self, driver):
        self.driver = driver


    def click_all_courses_link(self):
        self.driver.find_element(*self.lnk_all_courses).click()


    def click_sign_in_button(self):
        self.driver.find_element(*self.btn_sign_in).click()



