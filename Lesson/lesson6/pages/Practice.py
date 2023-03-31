from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class Practice:

    btn_hide = (By.ID, "hide-textbox")
    btn_show = (By.ID, "show-textbox")
    field_hide_show_example = (By.XPATH, "//*[@id='displayed-text']")
    dropbtn_mousehover = (By.ID, "mousehover")
    txt_footer = (By.CSS_SELECTOR, "div> div:nth-child(1) >p")
    top_option = (By.XPATH, "//a[text() = 'Top']")

    def __init__(self, driver):
        self.driver = driver


    def click_show_btn(self):
        self.driver.find_element(*self.btn_show).click()

    def click_hide_btn(self):
        self.driver.find_element(*self.btn_hide).click()

    def select_top_of_mousehover(self):
        self.driver.find_element(*self.dropbtn_mousehover).click()
        self.driver.find_element(*self.top_option).click()


    def get_alert_text(self):
        btn_alert = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "alertbtn")))
        btn_alert.click()
        popup = self.driver.switch_to.alert
        text = popup.text
        popup.accept()
        return text


    def get_attribute_hide_show_example_field(self):
        return self.driver.find_element(*self.field_hide_show_example).get_attribute("style")


    def get_footer_text(self):
        return self.driver.find_element(*self.txt_footer).text

