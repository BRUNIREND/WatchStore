from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from .forms import ProductForm
from .models import Products
from django.views.generic import DetailView, UpdateView, DeleteView


def catalog(request,category_slug="all", page=1):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)

    current_page = paginator.page(page)
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "product/products.html", context=context)


def ProductDelete(request, product_slug):

    if request.GET:
        model = Products.objects.filter(slug=product_slug).delete()

        return redirect('home')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
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