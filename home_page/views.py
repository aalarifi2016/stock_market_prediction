from django.shortcuts import render
from django.http import HttpResponse
from .models import get_price, get_news
# Create your views here.


def home_view(request):

    if request.method == "POST":
        price = get_price(request.POST.get('ticker'))
        news = get_news(request.POST.get('ticker'))

        # format the news
        news = [a['content'] for a in news['articles']]
        
        return render(request, 'home.html', {"price": price, "news": news})

    return render(request, 'home.html', {})


def about_view(request):
    return HttpResponse ('<p>about</p>')