from django.db import models
# from class_app.models import Clas

class Category(models.Model) :
    name = models.CharField( default="" ,  max_length=50)
    def __str__(self) -> str:
        return self.name
    # clas = models.ForeignKey(Clas , verbose_name= "class"  , on_delete=models.CASCADE )
# Create your models here.
