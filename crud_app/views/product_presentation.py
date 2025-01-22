from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    context = {}
    render(request, "product_presentaion/show.html", context)
    
def get(request):
    context = {}
    render(request, "product_presentaion/show.html", context)

def create(request):
    context = {}
    render(request, "product_presentaion/show.html", context)
    
    
def delete(request):
    context = {}
    render(request, "product_presentaion/show.html", context)
    
    
def update(request):
    context = {}
    render(request, "product_presentaion/show.html", context)
    
