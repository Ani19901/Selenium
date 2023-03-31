from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from lib import driver
from lib import test_logger

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


def find_elements(loc, timeout=10, get_text="", get_attribute=""):
    elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc))
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem


def fined_and_select(loc, timeout=10, text="Alabama"):
    select_element = find(loc, timeout)
    select_object = Select(select_element)
    select_object.select_by_visible_text(text)


def get_text_of_elements(loc):
    try:
        elements = driver.find_elements(*loc)
        text = []
        for i in elements:
            text.append(i.text)
        return text
    except Exception as e:
        print(e)


def create_dict_from_list(l1, l2):
    res = {l1[i]: l2[i] for i in range(len(l1))}
    return res


def write_in_file(text):
    try:
        with open("file", "a") as f:
            f.write(text + "\n ")
    except Exception as e:
        test_logger.logger(e)


# def upload_file(FileName, waitingTime):
#
# if FileName:
#
#     data_file = get_file_in_temp_folder(FileName)
#     actions.send_keys(UPLOAD_MODAL_FILE_, data_file)
#     actions.wait(1)
#     actions.wait_for_element_present(UPLOAD_MODAL_FILE_BTN, waitingTime)
#     actions.click(UPLOAD_MODAL_FILE_BTN)
#     else:
#     print("File is required, but missing\n")
