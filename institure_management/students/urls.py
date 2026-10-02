from django.urls import path
from students.views import *

urlpatterns = [
    path('students/', students_list, name='students_list'),
    path('students_regester/', add_students, name='add_students'),
]

