from django.urls import path
from cupon_app.views import cupon_list

urlpatterns = [
    path('' , cupon_list),
]