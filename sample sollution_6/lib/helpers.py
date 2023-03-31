from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lib.driver import get_driver

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


def switch_window(window_id=0):
    driver.switch_to.window(driver.window_handles[window_id])


def switch_to_alert():
    return driver.switch_to.alert
