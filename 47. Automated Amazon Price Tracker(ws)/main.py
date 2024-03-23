from bs4 import BeautifulSoup
import requests
from smtplib import SMTP

# Set up your email credentials and product URL
my_email = "your_email@gmail.com"
my_password = "your_email_password"
PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Set the request headers to mimic a web browser
request_headers = {
    "User-Agent": "Your-User-Agent-String",
    "Accept-Language": "en-US,en;q=0.9"
}

# Send a GET request to the product URL and retrieve the HTML content
response = requests.get(PRODUCT_URL, headers=request_headers)
response.raise_for_status()
html_doc = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_doc, "html.parser")

# Extract the price of the product
price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_in_float = float(price_without_currency)
print(price_in_float)

# Extract the product title
product = soup.find(id="productTitle").get_text().strip()
print(product)

BUY_PRICE =100
# Check if the price is below BUY_PRICE and send an email if it is
if price_in_float<BUY_PRICE:
    with SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(
            user = my_email,
            password= my_password,
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs="recipient@example.com",
            msg=f"Subject:Amazon Price Alert! \n\nGo and buy now!😉 \n{product} at {price}\nHere is the link to the product :"
                f"{PRODUCT_URL}".encode("UTF-8")
        )
