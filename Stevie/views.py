from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Post, Calendar
# Create your views here.


def index(request):
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='HM')
    context = {'post' : post, 'title': '- The Website', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def venues(request):   
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI') 
    post = Post.objects.filter(page='VN')
    context = {'post' : post, 'title': '- Where I Call', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def calendar(request):
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='CL')
    context = {'post' : post, 'title': '- Calendar', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def essense(request):
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='ES')
    context = {'post' : post, 'title': '- esSense', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

def newsnnotes(request):
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='NN')
    context = {'post' : post, 'title': '- NEWS\'n NOTES', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context)