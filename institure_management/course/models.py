from django.db import models
from teachers.models import TeacherModel
from students.models import StudentModel


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
    
class CourseEnrollModel(models.Model):
    student = models.ForeignKey(
        StudentModel,
        on_delete=models.SET_NULL,
        related_name='student_enrollment',
        null=True
    )
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        null=True
    )
    admission_fee = models.FloatField(null=True, blank=True)
    pay = models.FloatField(null=True, default=0.0)
    due = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.student.name if self.student else 'Unknown Student'}"

    def save(self, *args, **kwargs):
        if self.course:
            if self.pk is None:
                self.admission_fee = self.course.course_fee
            
            pay_amount = self.pay if self.pay is not None else 0.0
            fee_amount = self.admission_fee if self.admission_fee is not None else 0.0
            self.due = fee_amount - pay_amount
            
        super().save(*args, **kwargs)

class AssignTeacherModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        null=True
    )
    
    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else 'No Teacher'
        course_title = self.course.title if self.course else 'No Course'
        return f'{teacher_name}-{course_title}'
