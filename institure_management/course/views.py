from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
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
    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Course Category Added Successfully :)')
            return redirect('course_category')
    else:
        form_data = CourseCategoryForm()
    context = {
        'form_data' : form_data,
        'page_title' : 'Add Course Category Information',
        'form_title':'Add Course Category',
        'form_btn': 'Add Category',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def edit_category(request, id):
    category = get_object_or_404(CourseCategoryModel, id=id)
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
@require_POST
def delete_category(request, id):
    category = get_object_or_404(CourseCategoryModel, id=id)
    category.delete()
    messages.success(request, 'Category Deleted Successfully :(')
    return redirect('course_category')



@login_required
def course_list(request):
    course_list_data = CourseModel.objects.all()
    context = {
        'course_list_data': course_list_data,
    }
    return render(request, 'course_list.html', context)

@login_required
def add_course(request):
    if request.method == 'POST':
        form_data = CourseForm(request.POST, request.FILES)
        if form_data.is_valid():
            course_list_data = form_data.save(commit=False)
            course_list_data.created_by = request.user
            course_list_data.save()
            messages.success(request, 'Course Added Successfully :)')
            return redirect('course_list')
    else:
        form_data = CourseForm()
    context = {
        'form_data' : form_data,
        'page_title' : 'Add Course Information',
        'form_title':'Add Course',
        'form_btn': 'Add Course',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def edit_course(request, id):
    course = get_object_or_404(CourseModel, id=id)
    if request.method == 'POST':
        form_data = CourseForm(request.POST, request.FILES, instance=course)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Course Updated Successfully :)')
            return redirect('course_list')
    else:
        form_data = CourseForm(instance=course)
    context = {
        'form_data' : form_data,
        'page_title' : 'Edit Course',
        'form_title':'Update Course Info',
        'form_btn': 'Update Course',
    }
    return render(request, 'master/base-form.html', context)


@login_required
@require_POST
def delete_course(request, id):
    course = get_object_or_404(CourseModel, id=id)
    course.delete()
    messages.success(request, 'Course Deleted Successfully :(')
    return redirect('course_list')
