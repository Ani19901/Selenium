from selenium.webdriver.common.by import By
from lib import helpers, test_logger
from testdata import test_data

#####  Locators  ########
field_first_name = (By.XPATH, '//*[@id="firstname"]')
field_last_name = (By.XPATH, '//*[@id="lastname"]')
field_address = (By.XPATH, '//*[@id="address1"]')
field_password = (By.XPATH, '//*[@id="passwd"]')
field_city = (By.XPATH, '//*[@id="city"]')
field_zip_code_postal = (By.XPATH, '//*[@id="postcode"]')
field_state = (By.XPATH, '//*[@id="id_state"]')
field_mobile_phone = (By.XPATH, '//*[@id="phone_mobile"]')
btn_register = (By.XPATH, '//*[@id="submitAccount"]/span/text()')
field_my_account = (By.XPATH, '//*[@id="center_column"]/h1')

######## Functions ##########


def fill_register_data():
    try:
        helpers.find_and_send_keys(field_first_name, test_data.first_name)
        helpers.find_and_send_keys(field_last_name, test_data.last_name)
        helpers.find_and_send_keys(field_address, test_data.address)
        helpers.find_and_send_keys(field_password, test_data.password)
        helpers.find_and_send_keys(field_city, test_data.city)
        helpers.find_and_send_keys(field_zip_code_postal, test_data.zip_code_postal)

        helpers.find_and_send_keys(field_state, test_data.state)
        helpers.find_and_send_keys(field_mobile_phone, test_data.mobile_phone)
        helpers.find_and_click(btn_register)
        #helpers.find_and_send_keys(field_my_account, test_data.my_account)
        test_logger.logger(f'Register data was filled')
    except Exception as e:
        test_logger.logger(e)



