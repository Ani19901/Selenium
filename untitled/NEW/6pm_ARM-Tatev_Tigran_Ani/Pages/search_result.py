from selenium.webdriver.common.by import By
from sixpm_ARM.TestData import test_data
from Helpers import helpers

input_search = (By.XPATH,'//*[@id="searchAll"]')
btn_search = (By.XPATH,'//*[@type="submit"]')
icon_favorites = (By.XPATH,'.//*[@class="uk-z yk-z"]')
chcbx_price = (By.XPATH,'.//*[@class="uk-z yk-z"]')
checking_results = (By.XPATH, "//*[contains(text(), 'You Might Like These Brands')]")
btn_price_under_50 = (By.XPATH, "//*[contains(text(), '$50 and Under Sunglasses')]")
btn_shop_by_price = (By.XPATH, "//*[contains(text(), 'Shop By Price')]")
chbx_calvin_klein = (By.XPATH, "//*[contains(text(), 'Calvin Klein')]") #TODO rmove hard code from here
search_results_ck = (By.XPATH, './/*[@class = "qk-z"]')


def search_item(text):
    helpers.find_and_send_keys(text, test_data.searched_text)
    helpers.find_and_click(btn_search)


def get_searched_results():  #TODO call in test case
    helpers.find_displayed_element(checking_results)


def select_price():
    helpers.find_and_click(btn_shop_by_price)
    helpers.find_and_click(btn_price_under_50)


def select_calvin_klein(): #TODO cal in test case
    helpers.find_and_click(chbx_calvin_klein)


def check_found_items_quantity(): #TODO call in test case
    helpers.find_elements_len(search_results_ck, 12)
