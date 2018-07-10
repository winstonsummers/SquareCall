from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.
def index(request):
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='HM')
    context = {'post' : post, 'title': '', 'side': side, 'info': info,}
    return render(request, 'Stevie/index.html', context) 

def venues(request):    
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='VN')
    context = {'post' : post, 'title': '-- Venues', 'side': side, 'info': info,}
    return render(request, 'Stevie/index.html', context) 

def calendar(request):
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='CL')
    context = {'post' : post, 'title': '-- Calendar', 'side': side, 'info': info,}
    return render(request, 'Stevie/index.html', context) 

def newsletter(request):
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='NL')
    context = {'post' : post, 'title': '-- esSence Newsletter', 'side': side, 'info': info,}
    return render(request, 'Stevie/index.html', context) 
