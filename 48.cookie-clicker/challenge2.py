from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Mansi")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Yadav")

email = driver.find_element(By.NAME, "email")
email.send_keys("mansi@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
