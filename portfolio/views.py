from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("We are is home")
def about(request):
    return HttpResponse("We are is about")
def contact(request):
    return HttpResponse("We are is contact")
