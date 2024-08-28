from django.urls import path 
from category_app.views import search_category , return_all_categorys 

urlpatterns = [
    path("" , return_all_categorys) ,
    path("search" , search_category) ,
]
