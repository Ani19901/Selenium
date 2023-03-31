from Pages import home_page
from Pages import bag
from Pages import Login
from Pages import search_result
from Helpers import helpers
from configurations import configs





def test_4():
    helpers.go_to_page(configs.website_url)
    home_page.login_page_navigation()
    Login.login(configs.email,configs.password)
    helpers.find_and_click(home_page.btn_accessories)
    helpers.find_and_click(search_result.btn_watches)
    actual_favorites_number = search_result.select_random_elem()
    helpers.find_and_click(search_result.icon_favorite)
    expected_favorites_number = helpers.get_text_of_element(search_result.favorite_result)
    Assert.assertEquals(actual_favorites_number + "items", expected_favorites_number)

if __name__ == '__main__':
    test_4()






