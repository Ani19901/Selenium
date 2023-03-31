
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
progress_bar_link = driver.find_element(By.XPATH, "//*[text()='Progress Bar']")
start_btn = driver.find_element(By.ID, "startButton")
stop_btn = driver.find_element(By.ID, "stopButton")
duration_result = driver.find_element(By.XPATH, "//*[@id='result']")


def click_progress_bar_link():
    progress_bar_link.click()


def click_start_btn():
    start_btn.click()


def click_stop_btn():
    stop_btn.click()


click_progress_bar_link()
click_start_btn()
click_stop_btn()
duration_result.is_displayed()