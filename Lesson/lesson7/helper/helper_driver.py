from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


    def setUp(self, env_url):
        self.driver.get(env_url)
        self.driver.maximize_window()

    def close_driver(self):
        self.driver.close()

    def quite_driver(self):
        self.driver.quit()