from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
import random # No need to import if you dont use it
import time # No need to import if you dont use it


# ==========================================================
# Logging configurations
logging.basicConfig(filename="out.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("http://www.uitestingplayground.com/")
driver.maximize_window()


# Assignment 01
# ================================================

lst_button_names = []

lnk_visibility = "//a[text()='Visibility']"
page_visibility = "//h3[text()='Visibility']"
visible_buttons_xpath = "//*[text()='Playground']/preceding::ul[1]/following::table/tbody/tr/td/button"
btn_hide = "//*[@id='hideButton']"
check_removed_button = "//*[@id='hideButton']/parent::td/following::td[1]" # not exact button, you get full td
zero_width_button = "//*[@class='btn btn-warning zerowidth']"
overlapped_button = "//*[@id='hidingLayer']"
opacity_button = "//*[@style='opacity: 0;']"
visibility_button = "//*[@style='visibility: hidden;']"
display_none_button = "//*[@style='display: none;']"
offscreen_button = "//*[@class='btn btn-info offscreen']"

try:
    logging.info(f"Found {lnk_visibility} element")
    driver.find_element(By.XPATH, lnk_visibility).click()
    logging.info(f"Click on the element {lnk_visibility}")
    assert (driver.find_element(By.XPATH, page_visibility))
    logging.info(f"Driver locates to the {page_visibility} page")

    visible_buttons = driver.find_elements(By.XPATH, visible_buttons_xpath)
    for i in visible_buttons:
        i.is_displayed()
        lst_button_names.append(i.text)

    logging.info(f"The list of visible buttons: \n {lst_button_names}")
    logging.info("Click on the 'Hide' button")
    driver.find_element(By.XPATH, btn_hide).click()

    # For the first button, I can't find better solution
    # we dont understand what you are checking here?, remove or Removed button? Any way with text you can't assert button
    assert 'Remove'
    logging.info("The button 'Remove' is hidden")

# This block is not correct, it always return element in Dom, you should check is displayed or not? No need again find_element via xpath
# ----------------------------------------------------------------------  
    hidden_buttons = [
                      zero_width_button,
                      overlapped_button,
                      opacity_button,
                      visibility_button,
                      display_none_button,
                      offscreen_button
                      ]

    for i in hidden_buttons:
        if driver.find_element(By.XPATH, i):
            logging.info(f"The {i} button is hidden successfully")
        else:
            logging.info(f"The {i} button is still displayed")
 # ----------------------------------------------------------------------  

    driver.close()

except AssertionError:  # why AssertionError only? you whole code is under try, you need Exveption instead of AssertionError
    logging.error(AssertionError)

if driver:
    driver.quit()

# Assignment 2:
# ================================================

lnk_progress_bar = "//a[@href='/progressbar']"
page_progress_bar = "//h3[text()='Progress Bar']"
btn_start_id = "startButton"
btn_stop_id = "stopButton"
progress_bar_id = "progressBar"
text_result = "//*[@id='result']"


try:
    logging.info("Open the Progress Bar page")
    driver.find_element(By.XPATH, lnk_progress_bar).click()
    driver.find_element(By.XPATH, page_progress_bar).is_displayed()
    logging.info("Click on the 'Start' button")
    driver.find_element(By.ID, btn_start_id).click()
    wait_time = random.randint(1, 17)   # Good point with random data
    logging.info(f"Wait {wait_time} seconds")
    time.sleep(wait_time)
    driver.find_element(By.ID, btn_stop_id).click()
    time.sleep(2)
    result_text = driver.find_element(By.XPATH, text_result).text
    duration = result_text.split("duration: ")[-1]
    logging.info(f"The Duration is: {duration}")
    percent = driver.find_element(By.ID, progress_bar_id).text
    logging.info(f"The Percent is: {percent}")

    driver.close()

except AttributeError:
    logging.error(AttributeError)

if driver:
    driver.quit()


# Assignment 3:
# ================================================

new_button_name = "New Button Name"
lnk_input_text_xpath = "//*[@href='/textinput']"
page_input_text_xpath = "//h3[text()='Text Input']"
inp_field_xpath = "//*[@id = 'newButtonName']"
btn_updating_xpath = "//*[@id = 'updatingButton']"


try:
    logging.info("Open the Text Input page")
    driver.find_element(By.XPATH, lnk_input_text_xpath).click()
    driver.find_element(By.XPATH, page_input_text_xpath).is_displayed()
    logging.info("Enter data on the 'Set New Button Name' input field")
    driver.find_element(By.XPATH, inp_field_xpath).send_keys(new_button_name)
    driver.find_element(By.XPATH, btn_updating_xpath).click()
    time.sleep(2)
    assert (new_button_name, driver.find_element(By.XPATH, btn_updating_xpath).text)
    logging.info("Button name updated successfully")

    driver.close()


except AttributeError:
    logging.error(AttributeError)

if driver:
    driver.quit()


# 1st assignement is not fully correct
# no need to specify exception type, as your code block is under one try
# Other part is very good, we like your homework :)