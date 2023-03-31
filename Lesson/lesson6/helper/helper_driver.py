from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:

    def __init__(self):
        print("Open ChromeDriver")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


    def setUp(self, env_url):
        print("Env URL ===> ", env_url)
        self.driver.get(env_url)
        self.driver.maximize_window()

    def close_driver(self):
        self.driver.close()

    def quite_driver(self):
        self.driver.quit()

    def navigate_to_new_tab(self):
        self.driver.execute_script('''window.open("http://www.google.com/","_blank");''')
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
