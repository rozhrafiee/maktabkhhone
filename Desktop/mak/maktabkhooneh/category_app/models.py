from django.db import models
from class_app.models import Class

class Category(models.Model) :
    name = models.CharField(verbose_name= "name", null= False , max_length=50)
    clas = models.ForeignKey(Class , verbose_name= "class"  , on_delete=models.CASCADE , related_name= "cls")
# Create your models here.
