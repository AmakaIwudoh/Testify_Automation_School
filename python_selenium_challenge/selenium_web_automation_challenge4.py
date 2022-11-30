# Navigate to https://www.bbc.com/ and print out the top 10 latest news from the home page.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_keys_to_check_weather(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")

    news = driver.find_element(By.LINK_TEXT, "News").click()
    print("News:", news)

    # 1st news
    first_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    print("1st News:", first_news.text)

    # # 2nd news
    second_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/a[1]")
    print("2nd News:", second_news.text)

    # 3rd news
    third_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/div[1]/a[1]")
    print("3rd News:", third_news.text)

    # # 4th News
    fourth_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[1]/a[1]")
    print("4th News:", fourth_news.text)

    # 5th News
    fifth_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[11]/div[1]/div[2]/div[1]/a[1]")
    print("5th News:", fifth_news.text)

    # 6th News
    sixth_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[13]/div[1]/div[1]/div[2]/div[1]/a[1]")
    print("6th News:", sixth_news.text)

    # 7th News
    seventh_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[5]/div[1]/div[2]/div[1]/a[1]")
    print("7th News:", seventh_news.text)

    # 8th News
    eighth_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[2]/div[1]/div[2]/div[1]/a[1]")
    print("8th News:", eighth_news.text)

    # 9th News
    ninth_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[3]/div[1]/div[2]/div[1]/a[1]")
    print("9th News:", ninth_news.text)

    # 10th News
    tenth_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[4]/div[1]/div[2]/div[1]/a[1]")
    print("10th News:", tenth_news.text)


if __name__ == '__main__':
    main()