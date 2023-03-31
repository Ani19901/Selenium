from lib import helpers, test_logger, driver
from pages import contact_us, home, sign_in
from testdata import test_data


def test():
    helpers.go_to_page(test_data.url)
    helpers.find_and_click(home.btn_login_sign_in)
    sign_in.sign_in()
    helpers.find_and_click(contact_us.btn_contact_us)
    helpers.find_and_click(contact_us.btn_submit)
    assert (test_data.error_message, 'Success')
    test_logger.logger(f"The error message is displayed {test_data.error_message}")

    driver.close_driver(driver)


if __name__ == '__main__':
    test()


