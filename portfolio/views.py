from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact

# Create your views here.

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        print(f'{name},{email},{phone},{msg}')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(msg)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            messages.success(request,"your call was sucessful")
            contact = Contact(name=name, email=email,phone=phone, content=msg)
            contact.save()

    return render(request,"contact.html")
