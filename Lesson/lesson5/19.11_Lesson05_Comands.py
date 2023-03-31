import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://courses.letskodeit.com/practice")


# locatotrs
btn_hide = (By.ID, "hide-textbox")
btn_show = (By.ID, "show-textbox")
field_hide_show_example = (By.XPATH, "//*[@id='displayed-text']")
dropbtn_mousehover = (By.ID, "mousehover")
txt_footer = (By.CSS_SELECTOR, "div> div:nth-child(1) >p")
btn_sign_in = (By.XPATH, "//a[text()='Sign In']")
field_email = (By.XPATH, "//*[@id='page']//form/div[1]/input")
field_password = (By.XPATH, "//*[@id='password']")
btn_login = (By.XPATH, "//*[@id='page']//form/div[4]//input")
input_google_search = (By.XPATH, ".//*[@role='search']//div/div/input")

out_file = "alert_text.txt"

# setup logging
logging.basicConfig(filename="log.file.alert",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='w')


# functions
def write_data_in_txt_file(element_list):
    with open(out_file, "w") as f:
        for i in element_list:
            f.writelines(str(i) + '\n')


def navigate_to_new_tab():
    driver.execute_script('''window.open("http://www.google.com/","_blank");''')
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)


def get_result_count():
    return len(driver.find_elements(By.XPATH, "//*[@id='rso']/div/div/div/div[1]"))



def fill_in_search_field(text):
    driver.find_element(*input_google_search).send_keys(text)
    driver.find_element(*input_google_search).send_keys(Keys.RETURN)


def get_invalid_message_text():
    txt_message = (By.XPATH, "//*[@id='page']//form/div[1]/span")
    return driver.find_element(*txt_message).text


def click_login_btn():
    driver.find_element(*btn_login).click()


def fill_in_email_field(email_text):
    driver.find_element(*field_email).send_keys(email_text)


def fill_in_password_field(password_text):
    driver.find_element(*field_password).send_keys(password_text)


def click_sign_in_button():
    driver.find_element(*btn_sign_in).click()


def get_footer_text():
    return driver.find_element(*txt_footer).text


def select_top_of_mousehover():
    driver.find_element(*dropbtn_mousehover).click()
    top_option = (By.XPATH, "//a[text() = 'Top']")
    driver.find_element(*top_option).click()


def click_show_btn():
    driver.find_element(*btn_show).click()


def get_attribute_hide_show_example_field():
    return driver.find_element(*field_hide_show_example).get_attribute("style")


def click_hide_btn():
    driver.find_element(*btn_hide).click()


def get_alert_text():
    btn_alert = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "alertbtn")))
    btn_alert.click()
    popup = driver.switch_to.alert
    text = popup.text
    time.sleep(3)
    popup.accept()
    return text


# test

try:
    alert_popup_text = get_alert_text()
    logging.info(f"The Alert pop text is: {alert_popup_text}")

    click_hide_btn()
    logging.info(f"When clicking on the 'Hide' button the Attribute of the field is: {get_attribute_hide_show_example_field()}")
    click_show_btn()
    logging.info(f"When clicking on the 'Show' button the Attribute of the field is: {get_attribute_hide_show_example_field()}")

    select_top_of_mousehover()
    logging.info(f"The 'Top' of the MouseHover is selected")

    footer_text = get_footer_text()
    logging.info(f"The footer text is: {footer_text}")

    logging.info(f"Click on the 'Sign In' button, fill in the fields with invalid data and click on the 'Login' button")
    click_sign_in_button()
    fill_in_email_field("aaaa")
    fill_in_password_field("12")
    click_login_btn()
    #logging.info(f"The error mesage is: {get_invalid_message_text()}")

    logging.info(f"Navigate to new tab ")
    navigate_to_new_tab()
    fill_in_search_field("Automation")

    result_count = get_result_count()
    logging.info(f"The search result count is: {result_count} ")


    logging.info(f"The data are written in the txt file")
    write_data_in_txt_file([alert_popup_text, footer_text, result_count])

    logging.info(f"Close the opened tab")
    driver.close()

finally:
    driver.quit()
logging.info(f"The all tabs are closed")
