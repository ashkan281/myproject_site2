from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('login/' , views.show_login  , name="login"),
    path('logout' , views.user_logout , name="logout"),
]

