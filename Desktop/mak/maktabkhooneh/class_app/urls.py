from django.urls import path from .views import ClasList, ClasDetail, CreateClas, UpdateClas, DeleteClas, ClasDetailUpdateDelete
urlpatterns = [ path('', ClasList.as_view(), name='clas_list'),
               path('<int:pk>/', ClasDetail.as_view(), name='clas_detail'), 
               path('create/', CreateClas.as_view(), name='create_clas'),
               path('<int:pk>/update/', UpdateClas.as_view(), name='update_clas'),
               path('<int:pk>/delete/', DeleteClas.as_view(), name='delete_clas'),
               path('<int:pk>/detail-update-delete/', ClasDetailUpdateDelete.as_view(), name='clas_detail_update_delete'), ]
