from selenium.webdriver.common.by import By
from Helpers import helpers
from Helpers import driver
import random



#locators
search_results_ck = (By.XPATH, './/*[@class = "qk-z"]')  #TODO move to search_result
btn_add_to_bag = (By.XPATH, './/*[@data-track-value="Add-To-Cart"]')
btn_bag = (By.XPATH, './/*[@class = "B-z"]')
bug_price_item = (By.XPATH, './/*[@class="Zw-z bx-z"]')
bug_count_item = (By.XPATH, './/*[@id="quantity-B07VS374S9"]')
btn_x_on_bag = (By.XPATH, './/*[@class="jt-z"]')
btn_view_bag = (By.XPATH, '//*[@class="tt-z"]')
result_list = (By.XPATH, "//article[@itemtype='http://schema.org/Product']/a")
txt_empty_bag = (By.XPATH, "//*[@id='main']//p")
btn_remove = (By.XPATH, './/*[@aria-label="Remove Item"]')


# def add_item_to_bag():
# 	Helpers.find_items_from_list_and_click(search_results_ck, 0)
# 	Helpers.find_and_click(btn_add_to_bag)

def select_random_element():
    elems_count = helpers.find_elements(*result_list)
    elems_number = len(elems_count)
    random_item_number = random.randint(1, elems_number)
    elems_count[random_item_number].click()




