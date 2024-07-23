from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World you are at my first app home page.")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("This is about page of my application")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("This is the contact page of my application")
    return render(request, 'website/contact.html')

