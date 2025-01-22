from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    
    context = {}
    return render(request, "brand/show.html", context)
    
def get(request):
    context = {}
    return render(request, "brand/show.html", context)

def create(request):
    context = {}
    return render(request, "brand/show.html", context)
    
    
def delete(request):
    context = {}
    return render(request, "brand/show.html", context)
    
    
def update(request):
    context = {}
    return render(request, "brand/show.html", context)
    
