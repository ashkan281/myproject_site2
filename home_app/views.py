from django.shortcuts import render
from blog.models import artikle
# Create your views here.


def show_home(request):
    
    Artikle = artikle.objects.all()
    return render(request , 'home_app/index.html' , context={ 'Artikle': Artikle } )

