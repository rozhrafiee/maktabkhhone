from django.db import models
from teacher_app.models import  Teacher
from category_app.models import Category
from student_app.models import Student
class Class(models.Model) :
    name = models.CharField(max_length=50 )
    time = models.TimeField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)
    category = models.ForeignKey(Category , on_delete=models.CASCADE )
# Create your models here.
