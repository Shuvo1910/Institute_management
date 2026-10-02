from django.urls import path
from teachers.views import *

urlpatterns = [
    path('teachers/', teachers_list, name='teachers_list'),
    path('teachers_regester/', add_teachers, name='add_teachers'),
    path('edit-teacher/<int:pk>/', edit_teachers, name='edit_teachers'),
    path('delete-teacher/<int:pk>/', delete_teachers, name='delete_teachers'),

]
