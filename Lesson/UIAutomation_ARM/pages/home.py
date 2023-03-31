from lib import helpers, test_logger, driver
from selenium.webdriver.common.by import By



###########LOCATORS############
btn_contact_us = (By.XPATH,'.//*[@title ="Contact Us"]')
btn_dress = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]")

dress_name = (By.XPATH, '//*[@id="center_column"]/ul/li')
dress_price = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[1]/span[1]')

btn_login_sign_in = (By.XPATH, "//a[contains(text(),'Sign in')]")


def find_elements_titles_prices():

    titles = helpers.get_text_of_elements(dress_name)
    test_logger.logger(f"The titles is {titles}")
    prices = helpers.get_text_of_elements(dress_price)
    test_logger.logger(f"The prices is {prices}")
    test_logger.logger("The list of the titles and prices are added successfully")
    products = helpers.create_dict_from_list(titles, prices)
    test_logger.logger(f"The dictionry completed syccessfully {products}")
    helpers.write_in_file(f"This is product: {products}")





