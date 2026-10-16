from django.db import models
from user_auth.models import UserInfoModel

class CourseCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'
    
class CourseModel(models.Model):
    title = models.CharField(max_length = 200, null = True)
    description = models.TextField(null = True)
    category = models.ForeignKey(
        CourseCategoryModel,
        on_delete = models.SET_NULL,
        related_name = 'course_category',
        null = True,
    )
    course_fee = models.FloatField(null=True)
    course_module = models.TextField(null=True)
    course_thumbnail = models.ImageField(upload_to = 'media/course_img', null=True)
    credit = models.FloatField(null=True)
    created_by = models.ForeignKey(
        'user_auth.UserInfoModel',
        on_delete=models.SET_NULL,
        related_name='course_creator',
        null=True
    )
    
    def __str__(self):
        return f'{self.title}'

