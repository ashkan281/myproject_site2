from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout

# Create your views here.

def show_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        
        if user is not None:
            login(request , user)
            return redirect('home:home')
        
    return render(request , 'login_page/index.html' , context={})


def user_logout(request):
    logout(request)
    return redirect('home:home')