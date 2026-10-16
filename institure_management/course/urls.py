from django.urls import path
from course.views import *

urlpatterns = [
    #-------------- Course Category URL --------------#
    path('course-category/', course_category, name ='course_category'),
    path('add-category/', add_category, name ='add_category'),
    path('edit-category/<int:id>/', edit_category, name='edit_category'),
    path('delete-category/<int:id>/', delete_category, name='delete_category'),
    
    #-------------- Course URL --------------#
    path('course-list/', course_list, name='course_list'),
    path('course/add/', add_course, name='add_course'),
    path('course/edit/<int:id>/', edit_course, name='edit_course'),
    path('course/delete/<int:id>/',delete_course, name='delete_course'),
    
]
