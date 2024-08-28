from django.urls import path
from class_app.views import class_list , create_class , update_price

urlpatterns = [
    path('class-lists' , class_list),
    path('create-clas' , create_class),
    path('update-price/<str:inp_id>' , update_price)
]