import smtplib
import datetime as dt
import random

my_email="my697253@gmail.com"
password="xxfrwtezcpgvqgls"

#my697253 this is the identity of my email account and the part outside the @ i.e. gmail.com is the identity of my email provider
#if ur  email ends with gmail.com then this will be how u will connect to ur email server
# "smtp.gmail.com" location of our email provider smtp server
#tls stands for transport layer security and it's a way of securing our connection to our email server
#so the message will be encrypted nd will be impossible to read


with open("quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)
now = dt.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mansiemail23@gmail.com",
                            msg=f"subject:Monday Motivation\n\n{quote}")



