from django.shortcuts import render
from django.http import HttpResponse
from libs.get_data import Ticker
from libs.ML_model import predict_price
import pandas as pd


def home_view(request):

    # read the input from the user
    if request.method == "POST":
        ticker = request.POST.get("ticker").upper()
        print((ticker.upper()))
        data = Ticker(ticker)
        price = data.get_price()
        news = data.get_recent_news(source="reuters")
        file_csv = pd.read_csv("csv_data/reuters_news.csv")
        prediction = predict_price(file_csv, ticker)

        return render(
            request,
            "home.html",
            {"price": price, "news": news, "prediction": prediction},
        )

    return render(request, "home.html", {})


def about_view(request):
    return HttpResponse("<p>about</p>")
