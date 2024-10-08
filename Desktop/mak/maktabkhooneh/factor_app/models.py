from django.db import models
from cupon_app.models import Cupon
from class_app.models import Clas

class Factor(models.Model) :
    student_name = models.CharField(max_length=50)
    price = models.FloatField()
    cupon = models.OneToOneField(Cupon, on_delete=models.PROTECT)
    class1 = models.ForeignKey(Clas,default= '', on_delete=models.CASCADE)
    payment_status = models.BooleanField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        verbose_name = "Factor"
        verbose_name_plural = "FACTORS"
