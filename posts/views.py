from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_home(request):
    return HttpResponse("<h1> Hello, The First~!</h1>")

# def post_two(request):
#     return HttpResponse("<h1> Hello, The Two 222~!")