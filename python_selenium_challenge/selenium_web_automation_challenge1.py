# Using the chrome browser navigate to https://www.facebook.com/
# fill in the email/phone and password text box then click the Login Button

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_elements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    form = driver.find_element(By.TAG_NAME, "form")
    send_keys_to_elements(driver.find_element(By.NAME, "email"), "amakaezika@gmail.com")
    send_keys_to_elements(driver.find_element(By.NAME, "pass"), "password")
    time.sleep(5)
    login = driver.find_element(By.NAME, "login").click()

    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    main()