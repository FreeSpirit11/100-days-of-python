# Amazon Price Tracker

Welcome to the Amazon Price Tracker repository! This Python script monitors the price of a specific Amazon product. When the price drops below a set threshold, an email alert is sent.

## Getting Started


   ```shell
   git clone https://github.com/FreeSpirit11/100-days-of-python.git
   ```

2. Navigate to the directory containing the project files.
3. Install Python and required libraries: `pip install beautifulsoup4 requests`
4. **Replace the following variables with your own credentials:**

   - `my_email`: Your email address for sending alerts.
   - `my_password`: Your email password (use secure methods to store).
   - `PRODUCT_URL`: The URL of the Amazon product you want to track.
   - `BUY_PRICE`: Set the price threshold for receiving alerts.
   - `to_addrs` : Recipient email address.
   - `Your-User-Agent-String`: User agent string for mimicking a web browser.

5. Customize the request headers to mimic a web browser.
6. Run the script: `python main.py`
7. Stay updated with Amazon deals via email alerts!

## File Structure

- `main.py`: The main script file for tracking Amazon product prices and sending email alerts.
  
## Technologies Used

- Python
- BeautifulSoup
- SMTP (email)

## Disclaimer

Ensure compliance with Amazon's terms of use and use secure methods to store sensitive information.

## Acknowledgement

This project is a part of the "100 Days of Code" challenge by Angela Yu.

## Author
- [Mansi Yadav](https://github.com/FreeSpirit11/amazon-price-tracker)
