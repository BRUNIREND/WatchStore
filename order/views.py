from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, template_name='main/secondPage.html')


def order(request, id = None):

    context = {'id':id}
    return render(request, template_name='main/secondPage.html', context=context)
