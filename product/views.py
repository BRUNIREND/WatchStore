from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Products
from django.views.generic import DetailView, UpdateView, DeleteView
def catalog(request):
    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "product/products.html", context=context)




def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ProductForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'product/adminka_create.html', data)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "product/singleproduct.html", context=context)