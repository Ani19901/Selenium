import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Log information
logging.basicConfig(filename="log.file",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


def count_locators():
    list_for_search = []

    menu_elements = driver.find_elements(By.CSS_SELECTOR, ".submenu-with-border>li")
    search_field = driver.find_element(By.CSS_SELECTOR, "[class^='search']")
    search_button = driver.find_element(By.CSS_SELECTOR, "[class*='search']> div > form > button")
    home_page_buttons = driver.find_elements(By.CSS_SELECTOR, ".elementor-button-text")
    image_elements = driver.find_elements(By.CSS_SELECTOR, "[class*='link']>img")
    quik_view_icons = driver.find_elements(By.CSS_SELECTOR, ".astra-shop-thumbnail-wrap > a.ast-quick-view-text")
    grid_items = driver.find_elements(By.CSS_SELECTOR, "[class*='icon']>span")
    footer_links = driver.find_elements(By.CSS_SELECTOR, ".elementor-icon-list-items>li")

    list_for_search.append(search_field)
    list_for_search.append(search_button)

    print("Count of menu_elements are", len(menu_elements))
    print("Count of Home page buttons are", len(home_page_buttons))
    print("Count of Image elements are", len(image_elements))
    print("Count of Quik view elemens are", len(quik_view_icons))
    print("Count of Grid items are", len(grid_items))
    print("Count of footer links are", len(footer_links))
    print("Count of 'Search' field and 'Search' button", len(list_for_search))

    return len(menu_elements) + len(home_page_buttons) + len(image_elements) + len(quik_view_icons) + len(grid_items) + len(footer_links) + len(list_for_search)


try:
    driver.get("https://letskodeit.com/automationpractice/")
    driver.maximize_window()

    logging.info(f"Count of all elements on the Homepage are: {count_locators()}")

    driver.close()

except Exception as e:
    logging.error(e)
    driver.quit()
    exit(1)