from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Helpers import driver
from Helpers.driver import get_driver
from configurations import configs
from Helpers import test_logger
driver = get_driver()


def go_to_page(url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(loc, timeout=10):
    elem = find(loc, timeout)
    elem.click()

def find_displayed_element(loc, timeout=10):  # TODO duplicate with find
    elem = find(loc, timeout)
    #logger(f'Found element is {elem}')

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


def switch_window(window_id=0): # TODO extra
    driver.switch_to.window(driver.window_handles[window_id])


def switch_to_alert():# TODO extra
    return driver.switch_to.alert


def find_elements_len(item, count):
    elements = driver.find_elements(*item)
    #logger(f"Found elements quantity - '{len(elements)}'")
    elem_quantity = len(elements)
    assert (elem_quantity, count) #TODO no need assert in here, check in test case


def find_items_from_list_and_click(item, num): # TODO , not effective, try with for cycle
    elements = driver.find_elements(*item)
   # logger(f"Found elements quantity - '{len(elements)}'")
    product = elements[num]
    driver.click(product)

def verify_elements_texts(item, text): #TODO get_element_text
    elements = driver.find_element(item) #TODO why elements?
    #logger(f"Found elements quantity - '{len(elements)}'")
    assert (elements.text, text) #TODO no need assert in here, check in test case

#TODO Add find elements function
# remove all unnessacary methods
# add wait other options - like visibility, url_contains, etc...
# exceprtion handling is absent
