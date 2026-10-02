from django import forms
from django.db import transaction
from students.models import StudentModel
from user_auth.models import UserInfoModel

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()

    class Meta:
        model = StudentModel
        fields = ['username', 'email', 'name', 'address', 'phone', 'roll', 'image']
        exclude = ['user']
     
    @transaction.atomic   
    def save(self, commit=True):
        user = UserInfoModel.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='12345',
            user_type='Student'
        )
        
        student = super().save(commit=False)
        student.user = user
        
        if commit:
            student.save()
            
        return student
