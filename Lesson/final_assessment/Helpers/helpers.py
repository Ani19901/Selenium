import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from final_assessment.Helpers import log


def go_to_page(driver, url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find(driver, loc, timeout=10):
    try:
        elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc))
        log.logger(f"The '{loc}' is found")
        return elem
    except Exception as e:
        log.logger(e)


def find_and_click(driver, loc, timeout=10):
    elem = find(driver, loc, timeout)
    elem.click()
    log.logger(f"Click on '{loc}' element")


def find_and_send_keys(driver, loc, inp_text, timeout=10):
    try:
        elem = find(driver, loc, timeout)
        elem.send_keys(inp_text)
        log.logger(f"The '{inp_text}' entered in the '{loc}' field")

    except Exception as e:
        log.logger(e)


def find_elements(driver, loc, timeout=10):
    try:
        elems = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc))
        log.logger(f"The elements are found ")
        return elems
    except Exception as err:
        log.logger(err)


def json_data():
    with open('../conf.json', 'r') as f:
        data = json.load(f)
    return data


def update_json(email, password):
    try:
        with open('../conf.json') as f:
            data = json.load(f)
        data['email'] = email
        data['password'] = password
        with open('../conf.json', 'w') as f:
            json.dump(data, f)
        log.logger(" Json is updated")
    except Exception as err:
        log.logger(err)
