from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.
def index(request):
    post = Post.objects.filter(page='HM')
    context = {'post' : post, 'title': '',}
    return render(request, 'Stevie/index.html', context) 

def venues(request):
    post = Post.objects.filter(page='VN')
    context = {'post' : post, 'title': '-- Venues',}
    return render(request, 'Stevie/index.html', context) 

def calendar(request):
    post = Post.objects.filter(page='CL')
    context = {'post' : post, 'title': '-- Calendar',}
    return render(request, 'Stevie/index.html', context) 

def newsletter(request):
    post = Post.objects.filter(page='NL')
    context = {'post' : post, 'title': '-- esSence Newsletter',}
    return render(request, 'Stevie/index.html', context) 
