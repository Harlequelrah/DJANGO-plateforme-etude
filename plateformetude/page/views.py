from django.shortcuts import render

# Create your views here.
def index(request,*args,**kwargs):
    return  render(request,"index.html",{})

def home(request,*args,**kwargs):
    return  render(request,"home.html",{})

def login(request,*args,**kwargs):
    return  render(request,"login.html",{})
