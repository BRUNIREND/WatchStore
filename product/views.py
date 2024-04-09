from django.shortcuts import render

# Create your views here.
def pageOne(request, id=None):
    return render(request, "main/secondPage.html", context={"id": id})