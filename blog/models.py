from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# braye piade sakhi many to many 
class Category(models.Model):
    title = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.title

class artikle(models.Model):
    # 3 type model relation ship 
    # many to many realation ship 
    # many to one realation ship --> Forienkey 
    # one to one realation ship    
    
    
    # braye neveshtan author dastan intorie ke az ravesh manytoone estefade mishe yani 
    # be ezaye har ye user mitavan chandin ta mahgale dasht
    # one delete yani bad az inkke user pak shavad on hm pak mishe 
    
    
                                            # ( on_delete=model.set_null  , null=true )-->agar user pak shavad mitone null bashe 
                                            # ( on_delete=model.set_defult   , defult='yek meghdar bayd dashte bashe ' ) 
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=10 , unique=True , unique_for_date='pub_date') 
                                                                                    # ba neveshtan uniq for date dar yek roz faghat yek title mishe sakht 
                                                                                    # --> ba neveshtan uniq=true ... dar kol project faghat mitavan yek title dasht tekrari nmishe 
   
    category = models.ManyToManyField(Category)
   
    body = models.TextField()   
    image = models.ImageField(upload_to="images/artikle")
    # be sorat khodkar yek tarikh roz ro dorost mikone 
    created_time = models.DateTimeField(auto_now_add=True)
    # be sorat khodkar tarikh ghabl ro update mikone 
    update_time = models.DateTimeField(auto_now=True)
    
    # pub date tarikh roz ro migire 
    pub_date = models.DateField(default=timezone.datetime.now())
    
    # myfile = models.FileField(upload_to='images/resome' , null=True)
    
    
    
    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
    
       
    # file field hm gozine khobie braye download file and image or video ast 
    