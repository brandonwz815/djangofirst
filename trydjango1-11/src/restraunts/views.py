import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    num = None
    some_list = [
        random.randint(0, 1000000), 
        random.randint(0, 1000000), 
        random.randint(0, 1000000)
    ]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0, 1000000)
    context = {
        "bool_item": True,
        "num": num, 
        "some_list": some_list
    }
    return render(request, "base.html", context) 

def home2(request):
    context = {
    }
    return render(request, "home2.html", context) 
    
def home3(request):
    context = {
    }
    return render(request, "home3.html", context) 