# Using the firefox browser navigate to https://www.google.com/ enter the text Python in the search box,
# then  send  the  Enter  key.
# Get  the  text  from  the Wikipedia  brief  on  the  right  side  and  print the  value  in  the console.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_elements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    element = driver.find_element(By.TAG_NAME, "input")
    send_keys_to_elements(driver.find_element(By.NAME, "q"), "Python", Keys.ENTER)

    # driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    # driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)
    driver.close()

    print("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming")


if __name__ == '__main__':
    main()