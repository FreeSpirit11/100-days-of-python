from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")

HEADINGS = ["Rank", "Major", "Degree", "Early Career Pay(in $)", "Mid-Career Pay(in $)", "% High Meaning"]
with open("output.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(HEADINGS)

page=0
while True:
    tbody = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
    trows = tbody.find_elements(By.TAG_NAME, 'tr')
    with open("output.csv", 'a', newline='') as file:
        csv_writer = csv.writer(file)
        for trow in trows:
            spans = trow.find_elements(By.TAG_NAME, 'span')
            row_values = [int(span.text.replace('$', '').replace(',', '')) if "$" in span.text else span.text for span in spans if span.text]
            csv_writer.writerow(row_values)
    page += 1
    next_button = driver.find_element(By.CLASS_NAME, 'pagination__next-btn')
    if page != 31:
        next_button.click()
    else:
        print("Done.")
        break


driver.quit()