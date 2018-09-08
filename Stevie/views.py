from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Post, Calendar
# Create your views here.
cal = Calendar.objects.all()[:5]
side = Post.objects.filter(page='SB')
info = Post.objects.filter(page='CI')

def index(request):
    post = Post.objects.filter(page='HM')
    context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def venues(request):    
    post = Post.objects.filter(page='VN')
    context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def calendar(request):
    post = Post.objects.filter(page='CL')
    context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def essense(request):
    post = Post.objects.filter(page='ES')
    context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def newsnnotes(request):
    post = Post.objects.filter(page='NN')
    context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context)