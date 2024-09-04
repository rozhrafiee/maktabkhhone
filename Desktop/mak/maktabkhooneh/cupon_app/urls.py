from django.urls import path from .views import 
( CuponList, CuponDetail, CreateCupon, UpdateCupon, DeleteCupon, CuponDetailUpdateDelete, )
urlpatterns = [ path('cupons/', CuponList.as_view(), name='cupon-list'),
               path('cupons/<int:pk>/', CuponDetail.as_view(), name='cupon-detail'),
               path('cupons/create/', CreateCupon.as_view(), name='cupon-create'),
               path('cupons/update/<int:pk>/', UpdateCupon.as_view(), name='cupon-update'), 
               path('cupons/delete/<int:pk>/', DeleteCupon.as_view(), name='cupon-delete'),
               path('cupons/manage/<int:pk>/', CuponDetailUpdateDelete.as_view(), name='cupon-manage'), ]
