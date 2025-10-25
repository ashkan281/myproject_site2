from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class profiles(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    father_name = models.CharField(max_length=15)
    melicode = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/profile')
    
    
    
    # learning primary_key --> code meli mishe primary key 
    # for example : 
    # melicode = models.charfield(max_lenght = 50 , primary_key=true)
    # dar in model digar be jaye id ke be sorat khodkar dbsqlite primary_key klid asli ghrar midad 
    # ma be sorat dasri code meli o primary key ghrar dadim 
    
    
    
    def __str__(self):
        return self.user.username
    
        
