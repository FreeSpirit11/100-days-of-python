import os
from twilio.rest import Client
account_sid = "AC7f8efff16c7175a063e869b27fc0ff03"
auth_token = "6217de664ab2a17ba1e3957b31221e81"
import smtplib
my_email="my697253@gmail.com"
password="xxfrwtezcpgvqgls"
my_twilio_num = '+12542805765'

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message,user_num):
        message = self.client.messages \
            .create(
            body=message,
            from_=my_twilio_num ,
            to = user_num
        )
        

    def send_emails(self, message, user_email):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=user_email,
                                msg=message,
                                )


