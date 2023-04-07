from django.shortcuts import render
from django.http import HttpResponse
from .models import login
from django.contrib import messages
# Create your views here.

def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST.get('name')
        print(name)
        last_name = request.POST.get('last_name')
        print(last_name,'Last Name Printed')
        password = request.POST.get('password')
        content = request.POST.get('content')
        form = login.objects.create(
            username=username,
            email=email,
            name = name,
            last_name = last_name,
            password=password,
            content = content,
            )
        form.save()
        messages.success(request,'Your Form is Submit Successfully')
        return render(request,'formlogin.html',{'base': 'signup.html'})
    return render(request,'create.html')