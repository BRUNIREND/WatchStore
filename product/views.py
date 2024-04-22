from django.shortcuts import render
from django.http import HttpResponse
def products(request):
    return render(request, 'product/products.html', {'range': range(10)})
