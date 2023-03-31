from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Helpers import driver
from configurations import configs
from Helpers import test_logger
driver = driver.get_driver()



def go_to_page(url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(loc, timeout=10):
    elem = find(loc, timeout)
    elem.click()


def find_and_send_keys(loc, inp_text, timeout=10):
    elem = find(loc, timeout)
    elem.send_keys(inp_text)


def find(loc, timeout=10, get_text="", get_attribute=""):
    elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc))
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem



def find_elements_len(item, count):
    elements = driver.find_elements(*item)
    test_logger.logger(f"Found elements quantity - '{len(elements)}'")
    elem_quantity = len(elements)
    return elem_quantity



def get_text_of_element(item):
    try:
        element = driver.find_element(item).text
        return int(element)
    except Exception as e:
        print(e)

