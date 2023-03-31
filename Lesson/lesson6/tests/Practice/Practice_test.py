from lesson6.helper.helper_driver import Driver
from lesson6.helper.helper_write_data import WriteData
from lesson6.pages.ChromePage import ChromePage
from lesson6.pages.Login import Login
from lesson6.pages.Practice import Practice


def test():

    # create objects
    driver_obj = Driver()
    driver_obj.setUp("https://courses.letskodeit.com/practice")

    practice_obj = Practice(driver_obj.driver)
    login = Login(driver_obj.driver)
    chrome_page = ChromePage(driver_obj.driver)
    write_data = WriteData()

    get_logging = write_data.get_logging()

    try:
        # test
        get_logging.info(f"Get Pop up text")
        alert_popup_text = practice_obj.get_alert_text()
        get_logging.info(f"Click on the 'Show' button")
        practice_obj.click_show_btn()
        get_logging.info(f"Click on the 'Hide' button")
        practice_obj.click_hide_btn()
        get_logging.info(f"Get attribute of the 'Hide/Show Example' field")
        practice_obj.get_attribute_hide_show_example_field()
        get_logging.info(f"Select 'Top' of MouseHover")
        practice_obj.select_top_of_mousehover()
        get_logging.info(f"Get footer text")
        footer_text = practice_obj.get_footer_text()
        get_logging.info(f"Click on the 'Sign in' button")
        login.click_sign_in_button()
        get_logging.info(f"Select email field")
        login.fill_in_email_field("aa@mail.ru")
        get_logging.info(f"Select password field")
        login.fill_in_password_field("123")
        get_logging.info(f"Click on the 'Login' button")
        login.click_login_btn()
        #login.get_invalid_message_text()
        get_logging.info(f"Navigate to google")
        driver_obj.navigate_to_new_tab()
        get_logging.info(f"Search 'Automation'")
        chrome_page.fill_in_search_field("Automation")
        get_logging.info(f"Get Search result")
        result_count = chrome_page.get_result_count()

        get_logging.info(f"The data are written in the txt file")
        write_data.write_data_in_txt_file([alert_popup_text, footer_text, result_count])
        driver_obj.close_driver()

    finally:
        driver_obj.quite_driver()


if __name__ == '__main__':
    test()



