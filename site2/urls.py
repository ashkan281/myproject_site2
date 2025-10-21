from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home_app.urls')),
    path('' , include('login_page.urls')),
    path('' , include('register_page.urls')),
]


