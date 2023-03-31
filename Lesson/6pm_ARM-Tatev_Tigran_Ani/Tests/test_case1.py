from Pages import home_page
from Pages import Login
from Pages import search_result
from Helpers import helpers
from configurations import configs
from TestData import test_data


def test():
    helpers.go_to_page(configs.website_url)
    home_page.login_page_navigation()
    Login.login(configs.email,configs.password)
    search_result.search_item(test_data.searched_text)
    helpers.find(search_result.checking_results)
    search_result.select_price_under_50()
    helpers.find_and_click(search_result.chbx_calvin_klein)
    elems_count_actual = helpers.find_elements_len(search_result.search_results_ck, 12)
    elems_count_expected = helpers.get_text_of_element(search_result.txt_brands_counts)
    assert(elems_count_actual, elems_count_expected)



if __name__ == '__main__':
    test()



