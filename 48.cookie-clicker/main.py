from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME,"q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, "submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

#if none of these works xpath will work always
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close() #will close that particular tab which is open
driver.quit() #closes the entire browser





