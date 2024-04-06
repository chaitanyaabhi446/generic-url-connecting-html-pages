from django.shortcuts import render

# Create your views here.

def maggie(request):
    return render(request,'maggie.html')

def food(request):
    return render(request,'food.html')