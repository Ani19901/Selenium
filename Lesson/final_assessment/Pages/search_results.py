from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from final_assessment.Helpers import helpers


lnk_ultimate_qa = (By.XPATH, "//*[@title='Ultimate QA']")
inp_search_field = (By.XPATH, "//input[@type='search']")
arrow_next = (By.XPATH, "//a[@aria-label='Next page']")


def get_result_elements_titles(driver):
    page_elements = helpers.find_elements(driver, "//*[@id='main-content']//ul/li//h3")
    item_text_list = []
    for item in page_elements:
        item_text_list.append(item.text)
    while len(helpers.find_elements(driver, arrow_next)) > 0:
        helpers.find(driver, arrow_next).click()
        page_elements = helpers.find_elements(driver, "//*[@id='main-content']//ul/li//h3")
        for item in page_elements:
            item_text_list.append(item.text)
    return item_text_list


def search_data(driver, data):
    helpers.find_and_send_keys(driver, inp_search_field, data)
    element = helpers.find(driver, inp_search_field)
    element.send_keys(Keys.ENTER)


def search_for_non_existing_cource(driver):
    result_message = (By.XPATH, "//p[contains(@class, 'no-results')]")
    result = helpers.find_elements(driver, result_message)
    return len(result)