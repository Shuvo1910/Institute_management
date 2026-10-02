from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from teachers.models import TeacherModel
from teachers.forms import *
from django.contrib import messages

@login_required
def teachers_list(request):
    teachers_list = TeacherModel.objects.all()
    context = {'teachers_list' : teachers_list}
    return render(request, 'teachers-list.html', context)

@login_required
def add_teachers(request):
    form_data = TeacherForm()
    if request.method == 'POST':
        form_data = TeacherForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Teacher Register Successfully  :)')
            return redirect('teachers_list') 

    context = {
        'form_data' : form_data,
        'page_title' : 'Teacher Register',
        'form_title':'Add Teacher Info',
        'form_btn': 'Add Teacher',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def edit_teachers(request, pk):
    teacher = get_object_or_404(TeacherModel, pk=pk)
    
    if request.method == 'POST':
        form_data = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Teacher Updated Successfully  :)')
            return redirect('teachers_list')

    form_data = TeacherForm(instance=teacher)
        
    context = {
        'form_data' : form_data,
        'page_title' : 'Edit Teacher',
        'form_title':'Update Teacher Info',
        'form_btn': 'Update Teacher',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def delete_teachers(request, pk):
    teacher = get_object_or_404(TeacherModel, pk=pk)
    if teacher.user:
        teacher.user.delete()
    else:
        teacher.delete()
        
    messages.success(request, 'Teacher Deleted Successfully  :(')
    return redirect('teachers_list')
