import requests
from twilio.rest import Client
import random

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK = '05N3LOEWFLCXJ3UR'
NEWS_API = 'da59bb1bf0974a018e22ef57e709b515'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = ""
auth_token = ""

parameteres = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey': API_STOCK
}

response = requests.get("https://www.alphavantage.co/query",params=parameteres)
data = response.json()
days = data['Time Series (Daily)']
list_of_days = [day for day in days.items()]

yesterday = list_of_days[0]
yesterday2 = list_of_days[1]

yesterday_closing_price = float(yesterday[1]['4. close'])
yesterday2_closing_price = float(yesterday2[1]['4. close'])

absolute_differnce = abs(yesterday_closing_price - yesterday2_closing_price)

percentage_difference = absolute_differnce/yesterday_closing_price

news_parameteres = {
    'q':COMPANY_NAME,
    'searchIn':'title,description',
    'from':yesterday2[0],
    'apiKey':NEWS_API,
    'language':'en'
}

news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameteres)
news_articles = news_response.json()
list_of_articles = [news for news in news_articles.items()]

three_articles = list_of_articles[2][1][0:3]

random_article = {'title': three_articles[random.randint(0,2)]['title'],
                 'description': three_articles[random.randint(0,2)]['description']}

alert = f"{STOCK_NAME}: 🔺{percentage_difference * 100:.2f}%\nHeadline: {random_article['title']}\nBrief: {random_article['description']}"
if percentage_difference > 0.05 and yesterday_closing_price-yesterday2_closing_price>0:
    alert = f"{STOCK_NAME}: 🔺{percentage_difference * 100:.2f}%\nHeadline: {random_article['title']}\nBrief: {random_article['description']}"
elif percentage_difference > 0.05 and yesterday_closing_price-yesterday2_closing_price<0:
    alert = f"{STOCK_NAME}: 🔻{percentage_difference * 100:.2f}%\nHeadline: {random_article['title']}\nBrief: {random_article['description']}"

 
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14788886019',
  to='+48724876158',
  body=alert
)

