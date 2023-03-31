from final_assessment.Helpers import helpers, log
from final_assessment.Pages import basepage, sign_in, search_results
from final_assessment.TestData import testdata


def test_existing_cource(driver):
    """
    1 Go to page
    2. Search Any course
    3. Check searched course in found titles
    """
    data = helpers.json_data()
    helpers.go_to_page(driver, data["url"])
    helpers.find_and_click(driver, basepage.lnk_signe_in)
    sign_in.login(driver)
    search_results.search_data(driver, testdata.existing_search_data)
    all_results_titles = search_results.get_result_elements_titles(driver)
    for title in all_results_titles:
        assert testdata.existing_search_data in title
    log.logger("The appropriate result is displayed on the page")
