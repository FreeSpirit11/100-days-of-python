# use /robots.txt after the root website to check the website rules to scrape their data

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

zillow_url = "https://tinyurl.com/yc6fz5eb"
request_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9,hi;q=0.8"
}

response = requests.get(zillow_url, headers=request_headers)
response.raise_for_status()
zillow_html = response.text

soup = BeautifulSoup(zillow_html, 'html.parser')
all_listings = soup.find_all('article', {
    'data-test': "property-card",
})

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/1YXxmH0DAQPqX352UvXdOBswIs1k1YzDXUWkQOHsrY0k/edit?pli=1")

for listing in all_listings:
    link = listing.find('a', {'data-test':"property-card-link"}).get('href')
    if link[0] != 'h':
        link = "https://www.zillow.com" + link
    address = listing.find('address', {'data-test':"property-card-addr"}).text
    price = listing.find('span', {"data-test": "property-card-price"}).text

    time.sleep(20)
    property_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(address)

    property_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price.send_keys(price)

    property_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(link)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    time.sleep(10)
    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()






