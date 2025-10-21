from django.urls import path
from . import views


urlpatterns = [
    path('login/' , views.show_login ),
    path('logout' , views.user_logout),
]

