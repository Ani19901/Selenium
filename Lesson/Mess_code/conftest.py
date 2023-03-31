import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def driver():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as error:
        raise Exception(error)


@pytest.fixture()
def close_driver(driver):
    if driver:
        driver.close()

    
    


