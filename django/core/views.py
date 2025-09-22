from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('Hello!')
def home(request):
    return render(request, 'home.html', {'title': 'home'})
def base(request):
    return render(request, 'base.html', {'title': 'base'})
def about(request):
    return render(request, 'about.html', {'title' : 'about'})
