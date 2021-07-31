from django.shortcuts import render
from django.http import HttpResponse
from libs.get_data import Ticker


def home_view(request):

    # read the input from the user
    if request.method == "POST":
        ticker = request.POST.get("ticker").upper()
        print((ticker.upper()))
        data = Ticker(ticker)
        price = data.get_price()
        news = data.get_recent_news(source="reuters")

        return render(request, "home.html", {"price": price, "news": news})

    return render(request, "home.html", {})


def about_view(request):
    return HttpResponse("<p>about</p>")
