from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import datetime
from mailchimp3 import MailChimp

from .models import Post, Calendar
# Create your views here.

API_KEY = '0992de85e1ae5fcc1534597d2da7fc4d-us19'
LIST_ID = 'f93459e3a2'

def index(request):
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='HM')
    context = {'post' : post, 'title': '- The Website', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 

<<<<<<< HEAD

def venues(request):   
=======
def venues(request):    
>>>>>>> master
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

<<<<<<< HEAD

def essense(request):
<<<<<<< HEAD
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='ES')
    context = {'post' : post, 'title': '- esSense', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context) 
=======
# def essense(request):
#     post = Post.objects.filter(page='ES')
#     context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
#     return render(request, 'Stevie/essense.html', context) 

def essense(request):
=======
>>>>>>> master
    if request.method == 'GET':
        cal = Calendar.objects.all()[:5]
        side = Post.objects.filter(page='SB')
        info = Post.objects.filter(page='CI')
        post = Post.objects.filter(page='ES')
        context = {'post' : post, 'title': '', 'side': side, 'info': info, 'cal': cal}
        #if get, show past newsletters
        return render(request, 'Stevie/essense.html', context)
    elif request.method == 'POST':
        emailer = request.POST.get('name')
        email = request.POST.get('email')
        client = MailChimp(mc_api=API_KEY)
        client.lists.members.create(LIST_ID, {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': emailer,
            },
        })
        return redirect('essense')
<<<<<<< HEAD
>>>>>>> 1efacff7e0e3fbb60fde2431acc63c4cf2edfcb5

=======
>>>>>>> master

def newsnnotes(request):
    cal = Calendar.objects.all()[:5]
    side = Post.objects.filter(page='SB')
    info = Post.objects.filter(page='CI')
    post = Post.objects.filter(page='NN')
    context = {'post' : post, 'title': '- NEWS\'n NOTES', 'side': side, 'info': info, 'cal': cal}
    return render(request, 'Stevie/index.html', context)