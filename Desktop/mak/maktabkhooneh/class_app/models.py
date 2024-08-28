from django.db import models
from category_app.models import Category
class Clas(models.Model) :
    name = models.CharField(max_length=50 )
    time = models.TimeField()
    price = models.IntegerField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
# Create your models here.
