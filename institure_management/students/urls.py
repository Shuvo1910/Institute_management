from django.urls import path
from students.views import *

urlpatterns = [
    path('students/', students_list, name='students_list'),
    path('students_regester/', add_students, name='add_students'),
    path('edit-student/<int:pk>/', edit_student, name='edit_student'),
    path('delete-student/<int:pk>/', delete_student, name='delete_student'),

]

