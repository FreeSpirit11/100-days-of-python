import requests
api_key="33bad44293d4824631500d9f790516c0"
parameters={
            "lat":23.179300,
            "lon":75.784912,
            "appid":api_key
            }
response=requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice = wheather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

import os
from twilio.rest import Client
account_sid = 'AC7f8efff16c7175a063e869b27fc0ff03'
auth_token = '6217de664ab2a17ba1e3957b31221e81'

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today .Remember to bring an ☔ ",
        from_='+12542805765',
        to='+919399076738'
    )
print(message.status)
