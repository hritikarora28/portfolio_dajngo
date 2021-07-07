from django.db import models
from django.db.models.enums import IntegerChoices

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True);
    name = models.CharField(max_length=100);
    phone = models.IntegerField(max_length=13);
    email = models.EmailField(max_length=50)
    content = models.TextField();
    def __str__(self) :
        return 'Message from'+self.name


   

  
