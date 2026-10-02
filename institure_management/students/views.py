from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from students.models import StudentModel
from students.forms import *
from django.contrib import messages

@login_required
def students_list(request):
    students_list = StudentModel.objects.all()
    context = {'students_list' : students_list}
    return render(request, 'students-list.html', context)

@login_required
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

@login_required
def edit_student(request, pk):
    student = get_object_or_404(StudentModel, pk=pk)
    
    if request.method == 'POST':
        form_data = StudentForm(request.POST, request.FILES, instance=student)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Student Updated Successfully  :)')
            return redirect('students_list')

    form_data = StudentForm(instance=student)
        
    context = {
        'form_data' : form_data,
        'page_title' : 'Edit Student',
        'form_title':'Update Student Info',
        'form_btn': 'Update Student',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def delete_student(request, pk):
    student = get_object_or_404(StudentModel, pk=pk)
    if student.user:
        student.user.delete()

    student.delete()
        
    messages.success(request, 'Student Deleted Successfully  :(')
    return redirect('students_list')
    
