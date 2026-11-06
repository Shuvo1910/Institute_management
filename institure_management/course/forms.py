from django import forms
from course.models import *

class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategoryModel
        fields = '__all__'
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
        exclude = ['created_by']
        
class CourseEnrollForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollModel
        fields = '__all__'
        exclude = ['admission_fee', 'due']
        
class AssignTeacherForm(forms.ModelForm):
    class Meta:
        model = AssignTeacherModel
        fields = '__all__'