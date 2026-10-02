from django.shortcuts import render, redirect
from students.models import StudentModel
from students.forms import *
from django.contrib import messages

def students_list(request):
    students_list = StudentModel.objects.all()
    context = {'students_list' : students_list}
    return render(request, 'students-list.html', context)

def add_students(request):
    form_data = StudentForm()
    if request.method == 'POST':
        form_data = StudentForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Student Register Successfully  :)')
            return redirect('students_list') 

    context = {
        'form_data' : form_data,
        'page_title' : 'Student Register',
        'form_title':'Add Student Info',
        'form_btn': 'Add Student',
    }
    return render(request, 'master/base-form.html', context)
