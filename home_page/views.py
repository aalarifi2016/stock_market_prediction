from django.shortcuts import render
from django.http import HttpResponse
from libs.get_data import Ticker
# Create your views here.

from yahoo_fin import stock_info as si
# from newsapi import NewsApiClient

def get_price(ticker):

    #TODO: write a scrapping code to get the price from yahoo finance
    stock = si.get_live_price(ticker)

    # get stock price
    return round(stock, 2)

def get_news(ticker):
    #TODO: replace this api with scrapping tool to get the recent news from yahoo or reuters 
    data = Ticker(ticker)
    
    

    return []


def home_view(request):

    # read the input from the user
    if request.method == "POST":
        data = Ticker(request.POST.get('ticker'))
        price = get_price(request.POST.get('ticker'))
        news = data.get_recent_news(source='reuters')

        # format the news
        #TODO: this line needs to be replaced after fixing the get_news function
        # news = [a['content'] for a in news['articles']]
        
        return render(request, 'home.html', {"price": price, "news": news})

    return render(request, 'home.html', {})


def about_view(request):
    return HttpResponse ('<p>about</p>')