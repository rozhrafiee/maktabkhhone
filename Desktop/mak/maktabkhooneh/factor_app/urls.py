from django.urls import path from .views import 
( FactorList, FactorDetail, CreateFactor, UpdateFactor, DeleteFactor, FactorDetailUpdateDelete,
 CalculatePriceView, CreateFactorCustomView )
urlpatterns = [ path('factors/', FactorList.as_view(), name='factor-list'),
               path('factors/<int:pk>/', FactorDetail.as_view(), name='factor-detail'),
               path('factors/create/', CreateFactor.as_view(), name='factor-create'),
               path('factors/update/<int:pk>/', UpdateFactor.as_view(), name='factor-update'), 
               path('factors/delete/<int:pk>/', DeleteFactor.as_view(), name='factor-delete'),
               path('factors/manage/<int:pk>/', FactorDetailUpdateDelete.as_view(), name='factor-manage'), 
               path('factors/calculate-price/',
