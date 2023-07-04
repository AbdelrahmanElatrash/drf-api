from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    
    title=models.CharField(max_length=64)
    auther_name=models.CharField(max_length=64)
    release_date=models.DateField()
    img_url=models.URLField()
    description=models.TextField()
    user=models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    
    