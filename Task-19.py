from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class task19:
    username = "standard_user"
    passward = "secret_sauce"

    def __init__(self,web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def logging(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(self.username)
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.passward)
            self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
            sleep(3)

        except NoSuchElementException as selenium_error:
            print(selenium_error)

    def data_fetch(self):
        driver = self.driver
        webpage_title = driver.title
        current_url = driver.current_url
        webpage_content = driver.page_source
        with open("webpage_task_11.txt", "w", encoding="utf-8") as file:
            file.write(webpage_content)
        return webpage_title, current_url
        
url = "https://www.saucedemo.com/"
task = task19(url)
task.logging()
title, current_url = task.data_fetch()


print("Webpage Title:", title)
print("Current URL:", current_url)
print("Webpage content saved to 'webpage_task_11.txt'")
