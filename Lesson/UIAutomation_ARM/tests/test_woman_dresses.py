from pages import home
from lib import helpers
from testdata import test_data
from lib import driver


def test():
    helpers.go_to_page(test_data.url)
    helpers.find_and_click(home.btn_dress)
    home.find_elements_titles_prices()

    driver.close_driver(driver)


if __name__ == '__main__':
    test()
