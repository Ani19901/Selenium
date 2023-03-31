from final_assessment.Helpers import helpers, log
from final_assessment.Pages import sign_in, search_results, basepage
from final_assessment.TestData import testdata


def test_non_existing_cource(driver):
    """
    1. Go to Page
    2. Search not existing course
    3. Verify No Result Found message is visible
    """
    data = helpers.json_data()
    helpers.go_to_page(driver, data["url"])
    helpers.find_and_click(driver, basepage.lnk_signe_in)
    sign_in.login(driver)
    search_results.search_data(driver, testdata.non_existing_search_data)
    result_for_non_existing_cource = search_results.search_for_non_existing_cource(driver)
    assert result_for_non_existing_cource > 0
    log.logger("There is no any result for non existing data")