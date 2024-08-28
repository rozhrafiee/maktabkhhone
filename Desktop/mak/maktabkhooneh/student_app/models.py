from django.db import models

class Student(models.Model) :
    name = models.CharField(max_length=50 , null= False)
    email = models.EmailField(max_length=254 , null= False)
    phone_number = models.CharField(max_length=15 , null= False)
    clas = models.ManyToManyField('class_app.Class' , verbose_name="class" , related_name= "clss")
    cupon = models.ForeignKey('cupon_app.Cupon', on_delete=models.PROTECT , related_name= 'cupn')
    wallet = models.IntegerField(default= 0)
    
    def __str__(self) :
        return self.name 
# Create your models here.
                                                              