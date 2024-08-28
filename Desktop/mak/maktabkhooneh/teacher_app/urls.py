from django.urls import path 
from teacher_app.views import teacher_list , signup , average_rate

urlpatterns = [
    path("teacher_list" , teacher_list) , 
    path("signup" , signup) ,
    path("average_rate" , average_rate) ,
]