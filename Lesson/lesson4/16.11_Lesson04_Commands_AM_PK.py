import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


#driver = None
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.uitestingplayground.com/")


# locators
visibility_link = driver.find_element(By.XPATH, "//*[text()='Visibility']")
hide_btn = driver.find_element(By.XPATH, "//*[text()='Hide']")
removed_btn = driver.find_element(By.XPATH, "//*[text()='Removed']")
zero_width_btn = driver.find_element(By.XPATH, "//*[text()='Zero Width']")
overlapped_btn = driver.find_element(By.XPATH, "//*[text()='Overlapped']")
opacity_0_btn = driver.find_element(By.XPATH, "//*[text()='Opacity 0']")
visibility_hidden_btn = driver.find_element(By.XPATH, "//*[text()='Visibility Hidden")
display_none_btn = driver.find_element(By.XPATH, "//*[text()='Display None']")
offscreen_btn = driver.find_element(By.XPATH, "//*[text()='Offscreen']")


# log information
logging.basicConfig(filename="../log.file",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')


playground_btns = [removed_btn, zero_width_btn, overlapped_btn, opacity_0_btn, visibility_hidden_btn, display_none_btn, offscreen_btn]


# functions for UI WEB elements

def scroll_into_element(element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()


def click_visibility_link():
    visibility_link.click()
    print(driver.title)


def click_hide_button():
    hide_btn.click()


def is_displayed_playground_btns(playground_btns):
    for i in playground_btns:
        try:
            isDisplayed = i.is_displayed()
            logging.info(f"Displayed'{isDisplayed}' elements")

        except Exception as e:
            logging.error(e)


#scroll_into_element(visibility_link)
click_visibility_link()
is_displayed_playground_btns(playground_btns)
click_hide_button()


if driver:
    driver.quit()