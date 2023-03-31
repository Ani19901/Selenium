from lib import helpers
from lib import driver
from testdata import test_data
from pages import sign_up, home


def test_registration():
    helpers.go_to_page(test_data.url)
    helpers.find_and_click(home.btn_login_sign_in)
    sign_up.fill_register_data()

    driver.close_driver(driver)


if __name__ == '__main__':
    test_registration()


