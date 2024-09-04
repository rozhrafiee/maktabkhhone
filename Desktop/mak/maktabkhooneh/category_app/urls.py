from django.urls import path from .views import search_category, return_all_categories
urlpatterns = [ path('search/', search_category, name='search_category'),
               path('all/', return_all_categories, name='return_all_categories'), ]
