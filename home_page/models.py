from django.db import models

# Create your models here.
import yfinance as yf

def get_price(ticker):
    stock = yf.Ticker("AAPL")

    # get stock price
    return stock.info['previousClose']