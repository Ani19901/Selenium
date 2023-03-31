from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from webdriver_manager.chrome import ChromeDriverManager

# setup logging
logging.basicConfig(filename="log.file.alert",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='w')


# setup driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.uitestingplayground.com")
driver.maximize_window()


# ASSIGNMENT 1:
lnk_visibility = driver.find_element(By.XPATH, "//a[text()='Visibility']")
lnk_visibility.click()

btn_hide = driver.find_element(By.XPATH, "//*[@id='hideButton']")

btn_remove = (By.XPATH, "//*[@id='removedButton']")
zero_elem = (By.XPATH, "//*[@id='zeroWidthButton']")
btn_opacity = (By.XPATH, "//*[@id='transparentButton']")
visibility_hidden_elem = (By.XPATH, "//*[@id='invisibleButton']")
display_none_elem = (By.XPATH, "//*[@id='notdisplayedButton']")
offscreen_elem = (By.XPATH, "//*[@id='offscreenButton']")

hidden_buttons_list = [btn_remove, zero_elem, btn_opacity,
                        visibility_hidden_elem, display_none_elem, offscreen_elem]


btn_hide.click()


def find_hidden_element(element):
    try:
        element = driver.find_element(element)
        if not element:
            print(f"Not found")
        if not element.is_displayed():
            print(f"Element isn't displayed")
        else:
            print("Elements is displayed")

    except Exception as e:
        print(e)


for element in hidden_buttons_list:
    logging.info(f"{element} is displayed {find_hidden_element(element)}")

driver.back()


# ASSIGNMENT 3:
try:
    txt_input = driver.find_element(By.XPATH, "//a[text()='Text Input']")
    txt_input.click()
    time.sleep(3)

    entered_text = "aa"
    input_my_button = driver.find_element(By.XPATH, "//input[@placeholder= 'MyButton']")
    input_my_button.send_keys(entered_text)
    btn_change = driver.find_element(By.XPATH, "//*[@class = 'btn btn-primary']")
    btn_change.click()
    time.sleep(3)
    txt_chnaged = driver.find_element(By.XPATH, "//button[@id='updatingButton']").text

    if txt_chnaged == entered_text:
        logging.info(f"The button text is {txt_chnaged}")

except Exception as e:
    logging.error(e)

driver.back()

# ASSIGNMENT 2:
try:
    # Find "Progress Bar"
    lnk_progress_bar = driver.find_element(By.XPATH, "//a[text()='Progress Bar']")
    lnk_progress_bar.click()
    time.sleep(3)

    # Find "Start"
    btn_start = driver.find_element(By.XPATH, "//button[@id='startButton']")
    btn_start.click()
    time.sleep(3)

    # Find "Stop"
    btn_stop = driver.find_element(By.XPATH, "//button[@id='stopButton']")
    btn_stop .click()
    time.sleep(3)

except Exception as e:
    logging.error(e)

driver.quit()