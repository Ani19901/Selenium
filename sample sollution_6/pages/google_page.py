from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from lib import helpers
from lib.test_logger import logger
from testdata import test_data

txt_google_s = (By.XPATH, "//input[@name='btnK']//preceding::input[@type='text']")
google_result = (By.ID, "result-stats")


def google_search():
    helpers.go_to_page(test_data.google_url, new_window=True)
    helpers.switch_window(1)
    helpers.find_and_send_keys(txt_google_s, ('Automation', Keys.ENTER))
    found_result = helpers.find(google_result, get_text=True).split('(')[0]
    found_res_number = ''.join(filter(str.isdigit, found_result))
    logger(f'Google search result is - {found_res_number}')
    helpers.switch_window(0)
