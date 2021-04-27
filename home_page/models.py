from django.db import models


# Create your models here.
from yahoo_fin import stock_info as si
from newsapi import NewsApiClient


def get_price(ticker):
    #TODO: write a scrapping code to get the price from yahoo finance
    stock = si.get_live_price(ticker)

    # get stock price
    return round(stock, 2)

def get_news(ticker):
    #TODO: replace this api with scrapping tool to get the recent news from yahoo or reuters 
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