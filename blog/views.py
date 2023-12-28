from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_content(request):
    return HttpResponse("Hello, Blog!")