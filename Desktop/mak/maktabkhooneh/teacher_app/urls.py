from django.urls import path 
from teacher_app.views import teacher_list , signup , average_rate

urlpatterns = [
    path("teacher-list" , teacher_list) , 
    path("signup" , signup) ,
    path("average-rate" , average_rate) ,
]