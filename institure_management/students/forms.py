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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
     
    @transaction.atomic   
    def save(self, commit=True):
        student = super().save(commit=False)
        
        if student.user:
            user = student.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.save()
        else:
            user = UserInfoModel.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                password='12345',
                user_type='Student'
            )
            student.user = user
        
        if commit:
            student.save()
            
        return student
