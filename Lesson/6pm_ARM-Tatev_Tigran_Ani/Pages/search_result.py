from selenium.webdriver.common.by import By
from TestData import test_data
from Helpers import helpers
import  random

input_search = (By.XPATH, '//*[@id="searchAll"]')
btn_search = (By.XPATH, '//*[@type="submit"]')
icon_favorites = (By.XPATH, './/*[@class="uk-z yk-z"]')
chcbx_price = (By.XPATH, './/*[@class="uk-z yk-z"]')
checking_results = (By.XPATH, "//*[contains(text(), 'You Might Like These Brands')]")
btn_price_under_50 = (By.XPATH, './/a[@href="/sunglasses/CKzXARCq2QFqAQTiAgMBAg0.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/"]')
btn_shop_by_price = (By.XPATH, "//*[contains(text(), 'Shop By Price')]")
chbx_calvin_klein = (By.XPATH, './/*[@class="Lv-z"]')
search_results_ck = (By.XPATH, './/*[@class = "qk-z"]')
txt_brands_counts = (By.XPATH, '//*[@id="searchFilters"]//section[3]//ul/li[2]/a/span[2]')
btn_watches = (By.XPATH,'//*[@data-eventvalue="A-TOPCAT-WomensWatches"]')
icon_favorite = (By.XPATH, './/*[@class="A-z"]')
favorite_result = (By.XPATH, "//*[@title='Hearts']/span")



def search_item(text):
    helpers.find_and_send_keys(input_search, text)
    helpers.find_and_click(btn_search)


def select_price_under_50():
    helpers.find_and_click(btn_shop_by_price)
    helpers.find_and_click(btn_price_under_50)


def select_random_elem():
    btn_heart = (By.XPATH, f"(//*[@data-test-id='heartButton'])[{int}]")
    random_number = random.randint(1, 5)
    for i in range(random_number):
        helpers.find_and_click(btn_heart[i])
    return random_number