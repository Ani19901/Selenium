from selenium.webdriver.common.by import By
from sixpm_ARM.Helpers import helpers
from sixpm_ARM.Helpers import driver


#locators
search_results_ck = (By.XPATH, './/*[@class = "qk-z"]')  #TODO move to search_result
btn_add_to_bag = (By.XPATH, './/*[@data-track-value="Add-To-Cart"]')
btn_bag = (By.XPATH, './/*[@class = "B-z"]')
bug_price_item = (By.XPATH, './/*[@class="Zw-z bx-z"]')
bug_count_item = (By.XPATH, './/*[@id="quantity-B07VS374S9"]')
btn_x_on_bag = (By.XPATH, './/*[@class="jt-z"]')


def add_item_to_bag():
	helpers.find_items_from_list_and_click(search_results_ck, 0)
	helpers.find_and_click(btn_add_to_bag)
	#TODO add logging


def verify_bag_items():
	helpers.find_and_click(btn_bag)
	helpers.verify_elements_texts(bug_price_item, '$35.20') #TODO remove hard code from here
	helpers.verify_elements_texts(bug_count_item, 1)
	helpers.find_and_click(btn_x_on_bag)
	driver.back_driver() # TODO Incorrect
	helpers.find_items_from_list_and_click(search_results_ck, 0)
	helpers.find_and_click(btn_add_to_bag)
	helpers.find_and_click(btn_bag)
	helpers.verify_elements_texts(bug_price_item, '$70.40') #TODO remove hard code from here
	helpers.verify_elements_texts(bug_count_item, 2)
	#TODO add logging




