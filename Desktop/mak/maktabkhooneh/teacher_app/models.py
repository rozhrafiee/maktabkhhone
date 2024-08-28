from django.db import models
# from category_app.models import Category
from class_app.models import Clas

class Teacher(models.Model) :
    first_name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        help_text="Enter the first name of the teacher.",
        default= ""
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last Name",
        help_text="Enter the last name of the teacher." ,
        default= ""
    )
    email = models.EmailField(
        max_length=254,
        verbose_name="Email",
        help_text="Enter the Email of the teacher.",
        default=""
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Phone Number",
        help_text="Enter the phone number of the teacher.",
        default= ""
    )
    clas = models.ManyToManyField(
        Clas,
        related_name="teacher",
        verbose_name="Class",
        help_text="Enter the class of the teacher."
    )
    # category = models.ManyToManyField(
    #     Category,
    #     verbose_name="Category",
    #     help_text="Enter the category of the teacher."
    #     related_name= "category"
    # )
    rate = models.FloatField(
        verbose_name="Rate",
        help_text="Enter the rate of the teacher.",
        default= 0
    )

    wallet = models.FloatField(
        verbose_name="Wallet Balance",
        help_text="Enter the current balance in the teacher's wallet.",
        default=0
    )
    
    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"