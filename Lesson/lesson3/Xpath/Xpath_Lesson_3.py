from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging

driver = None
elements_count = 0
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://courses.letskodeit.com/practice")

# locator via Xpath
benz_checkbox = (By.XPATH, "//*[@id='benzradio']")
honda_select = (By.XPATH, "//*[contains(text(), 'Honda')]")
peach_multiple = (By.XPATH, "//*[contains(text(), 'Peach')]")
orange_multiple = (By.XPATH, "//*[contains(text(), 'Orange')]")
benz_radiobutton = (By.XPATH, "//*[@id='benzcheck']")
open_tab = (By.XPATH, "//*[@id='opentab']")
enter_your_name = (By.XPATH, "//*[@placeholder='Enter Your Name']")
web_table = (By.XPATH, "//td[contains(text(),'Python Programming Language')]")
show_element = (By.XPATH, "//*[@id = 'show-textbox']")
mouse_hover = (By.XPATH, "//*[text() = 'Mouse Hover Example']")
hide_show_example = (By.XPATH, "//*[@id='displayed-text']")


# log information
logging.basicConfig(filename="../log.file",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')

items = [benz_checkbox, honda_select, peach_multiple, orange_multiple, benz_radiobutton, open_tab, enter_your_name,
         web_table, show_element, mouse_hover, hide_show_example]


def test(item):
    elemetns = driver.find_elements(*item)
    logging.info(f"Fount the '{len(elemetns)}'")
    return len(elemetns)


for i in items:
    try:
        elements_count += test(i)
        logging.info(f"Success")

    except Exception as e:
        logging.error(e)

if driver:
    driver.quit()

logging.info(f"Found '{elements_count}' elements")