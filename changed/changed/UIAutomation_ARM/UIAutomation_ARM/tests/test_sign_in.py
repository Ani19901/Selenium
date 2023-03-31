from lib import driver
from pages import sign_in
from pages import home
from lib import helpers
from testdata import test_data


def test():
    helpers.go_to_page(test_data.url)
    helpers.find_and_click(home.btn_login_sign_in)
    sign_in.sign_in()

    driver.close_driver(driver)


if __name__ == '__main__':
    test()


