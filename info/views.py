from django.shortcuts import render
from info.models import *

# Create your views here.

def index(request):
    org = Org.objects.get(id=1)
    news = News.objects.all().order_by('-pubDate')[:5]
    releases = Release.objects.all().order_by('-release_date')[:5]
    return render(request, 'info/index.html', {'org': org, 'news': news, 'releases': releases})


def products(request):
    org = Org.objects.get(id=1)
    return render(request, 'info/products.html', {'org':org})


def services(request):
    org = Org.objects.get(id=1)
    return render(request, 'info/services.html', {'org':org})


def contacts(request):
    org = Org.objects.get(id=1)
    return render(request, 'info/contacts.html', {'org':org})


def about(request):
    org = Org.objects.get(id=1)
    return render(request, 'info/about.html', {'org':org})


def news(request):
    org = Org.objects.get(id=1)
    news = News.objects.all().order_by('-pubDate')
    return render(request, 'info/news.html', {'org': org, 'news': news})