from django.db import models
from class_app.models import Clas
from cupon_app.models import Cupon

class Student(models.Model) :
    name = models.CharField(max_length=50 )
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15 )
    clas = models.ManyToManyField(Clas, verbose_name="class" , related_name = "techer")
    cupon = models.ForeignKey(Cupon, on_delete=models.PROTECT)
    wallet = models.IntegerField(default= 0)
    
    def __str__(self) :
        return self.name 
# Create your models here.
                                                              