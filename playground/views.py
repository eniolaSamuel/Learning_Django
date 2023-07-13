from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse("Hello from the other side")


def hi(request):
    return render(request, 'greetings.html')
