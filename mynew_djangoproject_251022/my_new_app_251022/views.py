from django.http import HttpResponse
from django.shortcuts import render


def hello_page(request):
    return HttpResponse("Hello, it's our new web-site")
