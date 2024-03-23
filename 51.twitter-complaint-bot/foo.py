from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://facebook.com/")
# print("speed window")
# time.sleep(2)
#
# driver.execute_script("window.open('https://instagram.com/', '_blank');")
#
# print("instagram")

#can also send keys like control+tab to open a new tab