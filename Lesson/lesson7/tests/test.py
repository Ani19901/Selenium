import time

from lesson7.helper.helper_driver import Driver
from lesson7.pages.sign_up_page import SignUP
from lesson7.pages.sign_in_page import SignIn
from lesson7.pages.practice_page import Practice
from lesson7.pages.courses_page import Courses

first_name = "AA"
last_name = "BB"
email = "ab" + time.strftime("_%Y%m%d_%H%M%S") + "@gmail.com"
password = "123456"


def test():

    # create objects
    driver_obj = Driver()
    driver_obj.setUp("https://courses.letskodeit.com/practice")

    practice = Practice(driver_obj.driver)
    sign_up = SignUP(driver_obj.driver)
    sign_in = SignIn(driver_obj.driver)
    courses = Courses(driver_obj.driver)



    try:
        #test
        practice.click_sign_in_button()
        sign_in.click_sign_up_button()
        sign_up.fill_in_input_fields(first_name, last_name, email, password)
        sign_up.click_sign_up_button()
        sign_in.log_out()
        courses.click_sign_in_button()
        sign_in.fill_in_input_fields(email, password)
        sign_in.click_login_button()
        png_displayed = sign_in.user_profile_png_is_displayed()
        print("The user logged in is ", png_displayed)
        practice.click_all_courses_link()
        courses.fill_in_search_field("Selenium")
        time.sleep(3)
        result_count = courses.get_search_result_count()
        print("The result count is", result_count)
        result_amount = courses.get_search_result_amount()
        print("The result amounts are", result_amount)


    finally:
        driver_obj.quite_driver()


if __name__ == '__main__':
    test()



