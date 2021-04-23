from django.db import models


# Create your models here.
import yfinance as yf
from newsapi import NewsApiClient


def get_price(ticker):
    stock = yf.Ticker("AAPL")

    # get stock price
    return stock.info['previousClose']

def get_news(ticker):
    # Init
    newsapi = NewsApiClient(api_key='136424f10edd4de7b7f35adb9edaf0de')

    # /v2/everything
    all_articles = newsapi.get_everything(q=ticker,
                                        sources='bbc-news,the-verge',
                                        domains='bbc.co.uk,techcrunch.com',
                                        from_param='2021-04-09',
                                        to='2021-04-23',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)

    # /v2/sources
    sources = newsapi.get_sources()

    return all_articles