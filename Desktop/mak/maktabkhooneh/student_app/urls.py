from django.urls import path 
from student_app.views import return_all_students , list_class , signup , payment

urlpatterns = [
    path("" , return_all_students) ,
    path("class_list" , list_class) , 
    path("signup" , signup) ,
    path("payment" , payment)
]
