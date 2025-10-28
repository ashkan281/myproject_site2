from django.shortcuts import render
from blog.models import artikle
# Create your views here.


def show_detail_blog(request , pk): 
    Artikle = artikle.objects.get(id=pk)
    return render(request , 'blog/post_detail.html' , context={'Artikle' :Artikle }) 