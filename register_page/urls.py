from django.urls import path
from .  import views

app_name = "register" 
urlpatterns = [
    path('register' , views.show_register , name="registers"), # mitoni name ba url avalie motafavert bashe 
]
