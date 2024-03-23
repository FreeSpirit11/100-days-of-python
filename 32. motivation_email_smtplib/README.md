# Monday Motivation Email

This Python script sends motivational quotes via email every Monday to boost motivation and positivity. It uses the `smtplib` library to connect to an email server and sends the email using the `SMTP` protocol with TLS encryption for added security.


https://github.com/FreeSpirit11/100-days-of-python/assets/139609682/65ff50c3-2017-4b29-b879-87dc2d1342c9


## How it Works

The script reads a list of motivational quotes from the `quotes.txt` file. It then checks the current date, and if it's a Monday, it selects a random quote from the list and sends it via email to the recipient. The recipient's email address is specified as `to_addrs` in the `sendmail` function.

## Prerequisites

Before using the script, make sure to have Python installed on your system. You also need to have a Gmail account and enable "Allow less secure apps" or generate an "App password" for the script to send emails.

## How to Use

1. Clone this repository to your local machine or download the `quotes.txt` and `main.py` files.
2. Make sure you have Python installed on your system.
3. Open the `quotes.txt` file and add your favorite motivational quotes, one quote per line.
4. Replace the `MY_EMAIL` and `PASSWORD` variables in the `main.py` file with your Gmail account's email address and password or app password.
5. Run the script using the command: `python main.py`.
6. Check your email on Mondays to receive the motivational quote.

**Note:** For security reasons, avoid hardcoding your email and password in the script. Instead, consider using environment variables to store sensitive information.

## Customize the Schedule

If you want to change the schedule to a different day or time, modify the condition in the script that checks for Monday:

```python
if now.weekday() == 0:
```

Change `0` to the desired day of the week (0 for Monday, 1 for Tuesday, and so on).

## Acknowledgement

This project is a part of the "100 Days of Code" challenge by Angela Yu.

**Note to Users:**
If you have an email account other than Gmail, don't worry, this project can still work for you! The code uses Gmail's SMTP server to send emails, but you can easily adapt it to work with other email providers. All you need to do is replace `"smtp.gmail.com"` with the SMTP server of your email provider, and adjust the port number if necessary.

Please refer to your email provider's documentation or support resources to find the correct SMTP server and port for your email account. With a small modification to the code, you'll be able to enjoy the functionality of this project with your preferred email service. 

## Author

- [Mansi Yadav](https://github.com/FreeSpirit11)
