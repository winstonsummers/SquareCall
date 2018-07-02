from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.
def index(request):
    post = Post.objects.all()
    context = {'post' : post,}
    return render(request, 'Stevie/index.html', context) 

def venues(request):
    return HttpResponse("This will be the venues page.")

def calendar(request):
    return HttpResponse("This will be the calendar page.")

def newsletter(request):
    return HttpResponse("This will be the newsletter page.")
