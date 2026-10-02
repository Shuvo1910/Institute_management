from django.db import models
from user_auth.models import BasicInfoModel, UserInfoModel

class TeacherModel(BasicInfoModel):
    user = models.OneToOneField(
        UserInfoModel,
        on_delete=models.CASCADE,
        related_name = 'teacher_profile',
        null=True
    )
    joining_date = models.DateField(auto_now=True, null=True)
    image = models.ImageField(upload_to='media/teacher_img', null=True)
    
    def __str__(self):
        return f'{self.user.username}'