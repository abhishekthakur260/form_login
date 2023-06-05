from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View

# Create your views here.


class Login_View(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('logout/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
        
class Logout_View(View):
    # def get(self, request):
    #     logout(request)
    #     return redirect('login')
    
    def get(self, request):
        return render(request,'logout.html')
    

def register(request):

    if request.method=='POST':
        if 'register' in request.POST:
            user_type=request.POST.get('usertype')
            user_name=request.POST.get('userName')
            email=request.POST.get('email')
            first_name=request.POST.get('fname')
            last_name=request.POST.get('lname')
            password=request.POST.get('pwd')
            confirmPass=request.POST.get('confirm_pwd')
            authentication=Login.objects.filter(user_name=user_name)
            if authentication:

                msg="User name already taken"
            else:
                data=Login(user_name=user_name,password=password,first_name=first_name,last_name=last_name,
                           email=email,user_type=user_type,status='PENDING')
                data.save()
            
    return render(request,'register.html')
