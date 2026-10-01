from django.shortcuts import render
from students.models import StudentModel

def students_list(request):
    students_list = StudentModel.objects.all()
    
    context = {
        'students_list' : students_list,
        
    }
    
    return render (request, 'students-list.html', context)
