from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class artikle(models.Model):
    
    # braye neveshtan author dastan intorie ke az ravesh manytoone estefade mishe yani 
    # be ezaye har ye user mitavan chandin ta mahgale dasht
    # one delete yani bad az inkke user pak shavad on hm pak mishe 
    
    
                                            # ( on_delete=model.set_null  , null=true )-->agar user pak shavad mitone null bashe 
                                            # ( on_delete=model.set_defult   , defult='yek meghdar bayd dashte bashe ' ) 
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    body = models.TextField()
    image = models.ImageField(upload_to="images/artikle")
    # be sorat khodkar yek tarikh roz ro dorost mikone 
    created_time = models.DateTimeField(auto_now_add=True)
    # be sorat khodkar tarikh ghabl ro update mikone 
    update_time = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
    
       
    
    
# 3 type model relation ship 
# many to many realation ship 
# many to one realation ship --> Forienkey 
# one to one realation ship 
 