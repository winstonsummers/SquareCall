from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World!, This is Stephe's site.")

def venues(request):
    return HttpResponse("This will be the venues page.")

def calendar(request):
    return HttpResponse("This will be the calendar page.")

def newsletter(request):
    return HttpResponse("This will be the newsletter page.")
