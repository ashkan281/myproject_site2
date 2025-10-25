from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class profiles(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    father_name = models.CharField(max_length=15)
    melicode = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/profile')
    
    
    def __str__(self):
        return self.user.username
    
    
