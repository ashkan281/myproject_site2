from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
# Create your views here.

def show_register(request):
    contex = {
        'errors' : [],
    }
    if request.user.is_authenticated == True :
        return redirect('home:home')
        
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            contex['errors'].append("password is not a same ")
            return render(request , 'register_page/register.html' , contex)
                
        
        user = User.objects.create(
            username=username,
            password=password1,
            email=email
        )  
        login(request , user)
        return redirect('home:home')
    
    
    
    return render(request , 'register_page/register.html' , context={})