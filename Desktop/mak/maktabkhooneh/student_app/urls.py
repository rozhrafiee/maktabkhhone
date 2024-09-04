from django.urls import path from .views import ( StudentList, StudentDetail, CreateStudent, UpdateStudent,
StudentDetailUpdate, ListClassesByStudent, PaymentAPIView )
urlpatterns = [ path('students/', StudentList.as_view(), name='student-list'), 
               path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'), 
               path('students/create/', CreateStudent.as_view(), name='student-create'),
               path('students/<int:pk>/update/', UpdateStudent.as_view(), name='student-update'),
               path('students/<int:pk>/detail-update/', StudentDetailUpdate.as_view(), name='student-detail-update'),
               path('students/<str:student_name>/classes/', ListClassesByStudent.as_view(), name='student-classes'),
               path('students/payment/', PaymentAPIView.as_view(), name='student-payment'), ]
