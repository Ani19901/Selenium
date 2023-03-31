from Pages import home_page
from Pages import bag
from Pages import Login
from Pages import search_result
from Helpers import driver, helpers
from configurations import configs
from TestData import test_data


def test_3():
    helpers.go_to_page(configs.website_url)
    home_page.login_page_navigation()
    Login.login(configs.email, configs.password)
    search_result.search_item(test_data.searched_text)
    helpers.find(search_result.checking_results)
    bag.select_random_element()
    helpers.find_and_click(bag.btn_add_to_bag)
    helpers.find_and_click(bag.btn_view_bag)
    elem_price_in_bag = helpers.get_text_of_element(bag.bug_price_item)
    print(elem_price_in_bag)
    elem_count_in_bag = helpers.get_text_of_element(bag.bug_count_item)
    print(elem_count_in_bag)
    driver.back_driver()
    bag.select_random_element()
    helpers.find_and_click(bag.btn_add_to_bag)
    helpers.find_and_click(bag.btn_view_bag)
    assert (elem_count_in_bag, 2)
    helpers.find_and_click(bag.btn_remove)
    helpers.find(bag.txt_empty_bag)


if __name__ == '__main__':
    test_3()



