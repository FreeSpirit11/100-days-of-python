import requests
import datetime as dt
from twilio.rest import Client

TWILIO_PHONE_NUM = 'YOUR_TWILIO_PHONE_NUM'
RECEIVER_NUM = 'YOUR_PHONE_NUM'
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY="YOUR_STOCK_API_KEY"
NEWS_API_KEY="YOUR_NEWS_API_KEY"
STOCK_PARAMETERS={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}

now=dt.datetime.now()
current_date=now.date()
yesterday = current_date - dt.timedelta(days=1)
day_before_yesterday=yesterday-dt.timedelta(days=1)
if day_before_yesterday.weekday()==5:
    day_before_yesterday=day_before_yesterday-dt.timedelta(days=1)
if day_before_yesterday.weekday()==6:
    day_before_yesterday = day_before_yesterday - dt.timedelta(days=2)

stock_response=requests.get(url="https://www.alphavantage.co/query", params=STOCK_PARAMETERS)
stock_response.raise_for_status()
data=stock_response.json()
yesterday_closing_stock_price=data["Time Series (Daily)"][yesterday.strftime('%Y-%m-%d')]['4. close']
day_before_yesterday_stock_price=data["Time Series (Daily)"][day_before_yesterday.strftime('%Y-%m-%d')]['4. close']
percentage_change_in_stock_price=round(((float(day_before_yesterday_stock_price)-
                                   float(yesterday_closing_stock_price))/float(day_before_yesterday_stock_price))*100)
print(percentage_change_in_stock_price)
if abs(percentage_change_in_stock_price)>10:
    if percentage_change_in_stock_price<0:
        arrow="🔻"
    else:
        arrow="🔺"

    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    news_response=requests.get(url="https://newsapi.org/v2/everything", params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    articles=news_response.json()["articles"]

    for article in articles:
        news_title=article["title"]
        news_description=article["description"]
        news_url=article["url"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                body=f"{STOCK}: {arrow}{abs(percentage_change_in_stock_price)}%\n\nHeadline: {news_title}\n\nBrief: {news_description}\nurl: {news_url}",
                from_=TWILIO_PHONE_NUM,
                to=RECEIVER_NUM
            )


