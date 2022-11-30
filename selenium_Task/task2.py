import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def locate_by_xpath(driver):
   span = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div/div[1]/div/button/span[1]")
   print("Span:", span)
   #element = driver.find_element(By.XPATH, "/html/body/div/main/section[11]/div/div/div[1]/h2")
   #print("Element:", element)

def locate_by_tag_name(driver):
       second_element = driver.find_element(By.TAG_NAME, "h2")
       print("Second Element", second_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_xpath(driver)
    locate_by_tag_name(driver)


if __name__ == '__main__':
    main()