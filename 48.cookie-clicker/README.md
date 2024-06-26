# Automated Cookie Clicker with Selenium

This Python script automates the clicking of cookies and purchasing of items in the Cookie Clicker game using Selenium.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/2bbc5ab9-3080-4389-a61d-0c5c9ac720cb


## Description

The script navigates to the Cookie Clicker game hosted at [https://orteil.dashnet.org/experiments/cookie/](https://orteil.dashnet.org/experiments/cookie/) and automatically clicks on the cookie to earn money. It then determines the most expensive item that can be purchased with the current amount of money and buys it.

## Requirements

- Python 3.x
- Selenium library
- Chrome WebDriver

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install Selenium library using pip:

    ```bash
    pip install selenium
    ```

3. Download Chrome WebDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your system's PATH.

## Usage

1. Replace the path to the Chrome WebDriver in the script if necessary.
2. Run the script:

    ```bash
    python CookieClicker.py
    ```

## Notes

- The script automates the clicking of cookies and purchasing of items for five minutes.
- It utilizes the Chrome WebDriver for browser automation.
- Make sure to have a stable internet connection during script execution.

## Configuration

You can adjust the script's behavior by modifying variables like `five_min` (the duration of automation) and in-game item selection logic.

```python
# Customize the duration of automation (in seconds)
five_min = time.time() + 60

# Add or modify logic for in-game item selection
# Example:
# can_buy = {}
# for item in store:
#     item_money = int(item.text.split("-")[1].replace(",",""))
#     if current_money > item_money:
#         can_buy[item_money] = item
# can_buy[max(can_buy)].click()
```

## Acknowledgements

This project is inspired by the Cookie Clicker game and aims to showcase the capabilities of Selenium for web automation.

## Author

- [Mansi Yadav](https://github.com/FreeSpirit11/automated-game-playing-bot)
