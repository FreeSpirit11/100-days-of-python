from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os


PHONE_NUM = os.environ.get("PHONE_NUM")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://tinder.com/")

time.sleep(2)
privacy_accept = driver.find_element(By.XPATH, "//div[contains(@class, 'l17p5q9z') and text()='I decline']")
privacy_accept.click()

time.sleep(5)
log_in = driver.find_element(By.XPATH, "//*[contains(text(), 'Log in')]")
log_in.click()
time.sleep(15)

try:
    facebook_registration = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
    facebook_registration.click()
except NoSuchElementException:
    more_options = driver.find_element(By.XPATH, "//button[contains(text(), 'More options')]")
    more_options.click()
    time.sleep(5)
finally:
    facebook_registration = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
    facebook_registration.click()

time.sleep(10)

base_window = driver.window_handles[0]
fb_log_in_window = driver.window_handles[1]
driver.switch_to.window(fb_log_in_window)
print(driver.title)

time.sleep(10)
email = driver.find_element(By.ID, 'email')
email.send_keys(PHONE_NUM)
time.sleep(15)
password = driver.find_element(By.ID, 'pass')
password.send_keys(PASSWORD)
time.sleep(10)
password.send_keys(Keys.ENTER)

time.sleep(10)
driver.switch_to.window(base_window)
print(driver.title)

driver.maximize_window()

time.sleep(5)
location_accept = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location_accept.click()

time.sleep(10)
notifications_decline = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div/div[3]/button[2]')
notifications_decline.click()

while True:
    time.sleep(2)
    try:
        like_button = driver.find_element(By.XPATH,"//button[@type='button' and @class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a']")
        like_button.click()
        print('liked')
    except ElementClickInterceptedException:
        try:
            print('matched')
            time.sleep(5)
            match = driver.find_element(By.XPATH, "//button[@title='Back to Tinder' and contains(@class, 'C($c-ds-icon-secondary) Bdc($c-ds-icon-secondary) Bdc($c-ds-icon-secondary-inverse):h C($c-ds-icon-secondary-inverse):h close Cur(p) focus-button-style Scale(1.2)')]")
            match.click()
        except NoSuchElementException:
            pop_up = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'c1p6lbu0 D(b) Mx(a)')]")
            pop_up.click()






