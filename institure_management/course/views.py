from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from course.models import *
from course.forms import *
from django.contrib import messages

@login_required
def course_category(request):
    course_category_data = CourseCategoryModel.objects.all()
    context = {
        'course_category_data' : course_category_data,
    }
    return render(request, 'course_category.html', context)

@login_required
def add_category(request):
    form_data = CourseCategoryForm()
    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Course Category Added Successfully :)')
            return redirect('course_category')
    context = {
        'form_data' : form_data,
        'page_title' : 'Add Course Category Information',
        'form_title':'Add Course Category',
        'form_btn': 'Add Category',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def edit_category(request, pk):
    category = get_object_or_404(CourseCategoryModel, pk=pk)
    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST, instance=category)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Category Updated Successfully :)')
            return redirect('course_category')
    else:
        form_data = CourseCategoryForm(instance=category)
    context = {
        'form_data' : form_data,
        'page_title' : 'Edit Category Name',
        'form_title':'Update Category',
        'form_btn': 'Update Category',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def delete_category(request, pk):
    category = get_object_or_404(CourseCategoryModel, pk=pk)
    category.delete()
    messages.success(request, 'Category Deleted Successfully :(')
    return redirect('course_category')
