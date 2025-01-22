from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    greetings = "Hello, you are at index page"
    return JsonResponse(greetings, safe=False)


