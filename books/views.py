from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


# Create your views here.


def welcome(request):
    query_set = Author.objects.all()
    return render(request, 'welcome.html', {"authors": list(query_set)})


def hello(request):
    return HttpResponse("Hello from book app")


def books(request, pk):
    return HttpResponse(pk)
