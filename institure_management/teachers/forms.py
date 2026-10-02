from django import forms
from django.db import transaction
from teachers.models import TeacherModel
from user_auth.models import UserInfoModel

class TeacherForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()

    class Meta:
        model = TeacherModel
        fields = ['username', 'email', 'name', 'address', 'phone', 'image']
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
     
    @transaction.atomic   
    def save(self, commit=True):
        teacher = super().save(commit=False)
        
        if teacher.user:
            user = teacher.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.save()
        else:
            user = UserInfoModel.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                password='teacher',
                user_type='Teacher'
            )
            teacher.user = user
        
        if commit:
            teacher.save()
            
        return teacher
