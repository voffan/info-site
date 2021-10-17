from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'info/index.html')


def products(request):
    return  render(request, 'info/products.html')
