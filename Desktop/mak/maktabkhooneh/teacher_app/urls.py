from django.urls import path from .views import ( TeacherList, TeacherDetail, CreateTeacher, UpdateTeacher, DeleteTeacher,
TeacherDetailUpdateDelete, AverageRateAPIView, SortByRateAPIView, ) 
urlpatterns = [ path('', TeacherList.as_view(), name='teacher_list'),
               path('<int:pk>/', TeacherDetail.as_view(), name='teacher_detail'), 
               path('create/', CreateTeacher.as_view(), name='create_teacher'),
               path('<int:pk>/update/', UpdateTeacher.as_view(), name='update_teacher'),
               path('<int:pk>/delete/', DeleteTeacher.as_view(), name='delete_teacher'),
               path('detail-update-delete/<int:pk>/', TeacherDetailUpdateDelete.as_view(), name='teacher_detail_update_delete'),
               path('average-rate/', AverageRateAPIView.as_view(), name='average_rate'),
               path('sort-by-rate/', SortByRateAPIView.as_view(), name='sort_by_rate'), ]
