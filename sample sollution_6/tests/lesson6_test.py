from lib import helpers
from testdata import test_data
from pages import practice_page, sign_in_page, google_page


def test_5():
    helpers.go_to_page(test_data.practice_url)
    practice_page.save_alert_text()
    practice_page.hide_element_check()
    practice_page.mouse_hover_check()
    practice_page.footer_text()
    sign_in_page.sign_in()
    google_page.google_search()
    helpers.driver.quit()


if __name__ == '__main__':
    test_5()
