from django.shortcuts import render
from celeryproj.celery import add
from celeryapp.tasks import sub
# Create your views here.
def index(request):
    print("Results :")
    res = add.delay(10,20)
    print('add', res)
    
    res2 = sub.delay(10,20)
    print('sub', res2)
    return render (request , "celeryapp/home.html")

def about(request) :
    return render(request,"celeryapp/about.html")

def contact(request) :
    return render(request,"celeryapp/contact.html")