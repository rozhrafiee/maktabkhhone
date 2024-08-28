from django.db import models
from category_app.models import Category
from class_app.models import Class

class Teacher(models.Model) :
    first_name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        help_text="Enter the first name of the teacher."
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last Name",
        help_text="Enter the last name of the teacher."
    )
    email = models.EmailField(
        max_length=254,
        verbose_name="Email",
        help_text="Enter the Email of the teacher."
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Phone Number",
        help_text="Enter the phone number of the teacher."
    )
    clas = models.ManyToManyField(
        Class,
        related_name="Class",
        verbose_name="Class",
        help_text="Enter the class of the teacher."
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="Category",
        help_text="Enter the category of the teacher."
    )
    rate = models.FloatField(
        verbose_name="Rate",
        help_text="Enter the rate of the teacher."
    )

    wallet = models.FloatField(
        verbose_name="Wallet Balance",
        help_text="Enter the current balance in the teacher's wallet."
    )
    
    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"