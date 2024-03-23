from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# events={}
# for i in range(len(event_times)):
#     events[i]={"time ": event_times[i].text,
#          "name" : event_names[i].text}

events={i:{"time ": event_times[i].text, "name" : event_names[i].text} for i in range(len(event_times))}

print(events)