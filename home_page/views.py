from django.shortcuts import render
from django.http import HttpResponse
from .models import get_price
# Create your views here.


def home_view(request):

    if request.method == "POST":
        price = get_price(request.POST.get('ticker'))
        
        return render(request, 'home.html', {"price": price})

    return render(request, 'home.html', {})


def about_view(request):
    return HttpResponse ('<p>about</p>')