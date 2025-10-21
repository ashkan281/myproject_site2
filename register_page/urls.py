from django.urls import path
from .  import views

urlpatterns = [
    path('singin' , views.show_register , name="singin"), # mitoni name ba url avalie motafavert bashe 
]
