from django import forms
from course.models import *

class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategoryModel
        fields = '__all__'
        