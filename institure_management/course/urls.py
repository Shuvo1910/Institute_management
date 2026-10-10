from django.urls import path
from course.views import *

urlpatterns = [
    path('course-category/', course_category, name ='course_category'),
    path('add-category/', add_category, name ='add_category'),
    path('edit-category/<int:pk>/', edit_category, name='edit_category'),
    path('delete-category/<int:pk>/', delete_category, name='delete_category'),
    
]
