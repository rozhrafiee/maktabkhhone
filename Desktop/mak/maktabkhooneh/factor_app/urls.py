from django.urls import path
from factor_app.views import calculate_price, create_factor


urlpatterns = [
    path("cal-price", calculate_price),
]