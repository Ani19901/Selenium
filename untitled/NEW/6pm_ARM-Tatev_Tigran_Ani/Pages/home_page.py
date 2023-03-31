from random import random

from selenium.webdriver.common.by import By
from Helpers import helpers



icon_login = (By.XPATH, ".//*[@class='y-z']")
txt_accessories = (By.XPATH, "//*[@id='root']//header/div[2]/ul/li[4]")
txt_watches = (By.XPATH, "//*[@id='main']//div[2]//div/article[2]")
icon_favorite = (By.XPATH, "//*[@id='products']/article[1]/div[1]/div[1]/div")




def click_accessories():
    helpers.find_and_click(txt_accessories, timeout=10)


def click_watches():
    helpers.find_and_click(txt_watches, timeout=10)


def select_favorite_icon(x):
    for i in x:
        helpers.find_and_click(icon_favorite, timeout=10)


def get_len_favorite_items():
    elements_xpath = (By.XPATH, "//*[@id='products']/article//button")
    elements = driver.find_elements(*elements_xpath)
    return len(elements)


def click_random_favorites(elements_count, count):
    i = 0
    random_elements = random(1, elements_count + 1)
    random_favorites_element = (By.XPATH, f"//*[@id='products']/article[{random_elements}]//button")
    for i in count:
        helpers.find_and_click(random_favorites_element, timeout=10)
    return i





