#Navigate to the website https://academy.testifyltd.com/

#Get the element with the text "© 2022 Testify Limited. All rights reserved."

#Print out the element text, and properties, and it attributes

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#def print_element_fields(element):
    #print("Text:", element.text)
    #print("Size:", element.size)
    #print("Tag Name:", element.tag_name)
    #print("ID:", element.id)
    #print("Location:", element.location)
    #print("Accessible Name:", element.accessible_name)


def print_element_attributes(element):
        print("Text:", element.text)
        print("Class:", element.get_attribute("class"))
        print("Inner Text:", element.get_attribute("innertext"))
        print("Inner HTML:", element.get_attribute("innerhtml"))

def locate_element_properties(element):
        print("Class Property:", element.get_property("class"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_element_attributes(element)
    #print_element_fields(element)
    locate_element_properties(element)



if __name__ == '__main__':
    main()