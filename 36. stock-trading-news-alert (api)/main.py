import requests
import datetime as dt
from twilio.rest import Client

account_sid = 'AC7f8efff16c7175a063e869b27fc0ff03'
auth_token = '6217de664ab2a17ba1e3957b31221e81'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY="29WRHFUERRMPIMKV"
NEWS_API_KEY="a5b746556e2a4beda1c44e45529c1193"
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
                from_='+12542805765',
                to='+919399076738'
            )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling floato Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling floato Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

