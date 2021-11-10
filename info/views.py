from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
import os
from transliterate import translit
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


def courses(request):
    org = Org.objects.get(id=1)
    return render(request, 'info/courses.html', {'org': org})


def get_price_list(request):
    org = Org.objects.get(id=1)
    if os.path.exists(org.price_list.path):
        with open(org.price_list.path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/'+os.path.splitext(org.price_list.name)[1][1:])
            f_name = os.path.basename(org.price_list.name)
            response['Content-Disposition'] = 'attachment; filename=' + translit(f_name, "ru", reversed=True)
            return response
    return render(request, 'info/404.html', {'org': org})


class NewsListView(ListView):
    paginate_by = 15
    model = News
    template_name = 'info/news.html'
    ordering = ['-pubDate']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['org'] = Org.objects.get(id=1)
        return context


class ReleaseListView(ListView):
    paginate_by = 10
    model = Release
    template_name = 'info/releases.html'
    ordering = ['-release_date']

    def get_queryset(self):
        return Release.objects.select_related('program').filter(active=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['org'] = Org.objects.get(id=1)
        return context