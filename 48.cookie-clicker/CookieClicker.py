from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


def get_money():
    return int(driver.find_element(By.ID, "money").text.replace(",",""))

five_min = time.time() + 60
while time.time() <five_min:
    start_time = time.time()
    while (time.time() - start_time) <5:
        cookie.click()
    current_money = get_money()
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    store.pop()
    can_buy = {}
    for item in store:
        item_money = int(item.text.split("-")[1].replace(",",""))
        if current_money > item_money:
            can_buy[item_money] = item
    can_buy[max(can_buy)].click()

count = driver.find_element(By.ID, "cps").text
print(count)

