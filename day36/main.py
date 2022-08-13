import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
request = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={APIKey}")
request.raise_for_status()
stockdata = request.json()

def CheckStockPrice():
    todayprice = float(stockdata["Time Series (Daily)"]["2022-08-12"]["4. close"])
    yesterdayprice =float(stockdata["Time Series (Daily)"]["2022-08-11"]["4. close"])
    diff = abs(todayprice-yesterdayprice)
    if(diff >= todayprice/1000):
        if(todayprice > yesterdayprice):
            GetNews(True, diff*100/todayprice)
        else:
            GetNews(False, diff*100/todayprice)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
request = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NewsAPIKey}")
request.raise_for_status()
reqData = request.json()
def GetNews(increase : bool, diffperc : float):
    listNews =[]
    for i in range(0,3):
        listNews.append(reqData["articles"][i]["title"])
    if increase:
        print (f"Tesla up by {diffperc}%. News headlines are {listNews}")
    else:
        print(f"Tesla down by {diffperc}%. News headlines are {listNews}")


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:

CheckStockPrice()
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

