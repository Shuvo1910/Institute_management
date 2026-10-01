from django.db import models
from user_auth.models import BasicInfoModel, UserInfoModel


class StudentModel(BasicInfoModel):
    user = models.OneToOneField(
        UserInfoModel,
        on_delete=models.CASCADE,
        related_name = 'student_profile',
        null=True
    )
    roll = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/student_img', null=True)

    def __str__(self):
        return f'{self.user.username}'
