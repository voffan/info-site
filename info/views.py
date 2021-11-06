from django.shortcuts import render
from django.views.generic import ListView
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


class NewsListView(ListView):
    paginate_by = 15
    model = News
    template_name = 'info/news.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['org'] = Org.objects.get(id=1)
        return context


class ReleaseListView(ListView):
    paginate_by = 10
    model = Release
    template_name = 'info/releases.html'

    def get_queryset(self):
        return Release.objects.select_related('program').filter(active=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['org'] = Org.objects.get(id=1)
        return context