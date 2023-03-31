from pages import home
from lib import helpers
from testdata import test_data
from lib import driver
from pages import contact_us


def test():
    helpers.go_to_page(test_data.url)
    helpers.find_and_click(home.btn_login_sign_in)
    helpers.find_and_send_keys(contact_us.input_email, test_data.existing_username)
    helpers.find_and_send_keys(contact_us.input_order, test_data.order_ref)
    helpers.fined_and_select("Webmaster")
    helpers.find_and_click(contact_us.btn_submit)

    driver.close_driver(driver)


if __name__ == '__main__':
    test()
