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
    
    #-------------- Course Enrollment URL --------------#
    path('course-enroll/', course_enroll_list, name='course_enroll_list'),
    path('enroll-student/', enroll_new_student, name='enroll_new_student'),
    path('enroll/edit/<int:id>/', edit_enroll_info, name='edit_enroll_info'),
    path('enroll/delete/<int:id>/',delete_enroll_info, name='delete_enroll_info'),
    
    #-------------- Teacher Assignment URL --------------#
    path('assign-teacher/', assign_teacher_list, name='assign_teacher_list'),
    path('assign-new-teacher/', assign_new_teacher, name='assign_new_teacher'),
    path('assign-teacher/edit/<int:id>/', edit_assign_teacher_info, name='edit_assign_teacher_info'),
    path('assign-teacher/delete/<int:id>/', delete_assign_teacher_info, name='delete_assign_teacher_info'),

]
