from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from course.models import *
from course.forms import *
from django.contrib import messages

@login_required
def course_category(request):
    if request.user.user_type == 'Admin':
        course_category_data = CourseCategoryModel.objects.all()
        context = {
            'course_category_data' : course_category_data,
        }
        return render(request, 'course_category.html', context)
    else:
        return redirect('dashboard_view')
    
@login_required
def add_category(request):
    if request.user.user_type == 'Admin':
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
    else:
        return redirect('dashboard_view')

@login_required
def edit_category(request, id):
    if request.user.user_type == 'Admin':
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
    else:
        return redirect('dashboard_view')

@login_required
@require_POST
def delete_category(request, id):
    if request.user.user_type == 'Admin':
        category = get_object_or_404(CourseCategoryModel, id=id)
        category.delete()
        messages.success(request, 'Category Deleted Successfully :(')
        return redirect('course_category')
    else:
        return redirect('dashboard_view')

@login_required
def course_list(request):
    course_list_data = CourseModel.objects.all()
    context = {
        'course_list_data': course_list_data,
    }
    return render(request, 'course_list.html', context)

@login_required
def add_course(request):
    if request.user.user_type == 'Admin':
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
    else:
        return redirect('dashboard_view')

@login_required
def edit_course(request, id):
    if request.user.user_type == 'Admin':
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
    else:
        return redirect('dashboard_view')


@login_required
@require_POST
def delete_course(request, id):
    if request.user.user_type == 'Admin':
        course = get_object_or_404(CourseModel, id=id)
        course.delete()
        messages.success(request, 'Course Deleted Successfully :(')
        return redirect('course_list')
    else:
        return redirect('dashboard_view')

@login_required
def course_enroll_list(request):
    if request.user.user_type == 'Admin':
        enrolled_data = CourseEnrollModel.objects.all()
    elif request.user.user_type == 'Student':
        enrolled_data = CourseEnrollModel.objects.filter(student__user=request.user)
    else:
        enrolled_data = CourseEnrollModel.objects.none()

    context = {
        'enrolled_data': enrolled_data
    }
    return render(request, 'course-enroll-list.html', context)

@login_required
def enroll_new_student(request):
    if request.user.user_type == 'Admin':
        if request.method == 'POST':
            form_data = CourseEnrollForm(request.POST)
            if form_data.is_valid():
                form_data.save()
                messages.success(request, 'Student Enrolled Successfully :)')
                return redirect('course_enroll_list')
        else:
            form_data = CourseEnrollForm()
        context = {
            'form_data' : form_data,
            'page_title' : 'Course Enrollment Info',
            'form_title':'Course Enrollment',
            'form_btn': 'Enroll New Student',
        }
        return render(request, 'master/base-form.html', context)
    else:
        return redirect('dashboard_view')
    
@login_required
def edit_enroll_info(request, id):
    if request.user.user_type == 'Admin':
        course = get_object_or_404(CourseEnrollModel, id=id)
        if request.method == 'POST':
            form_data = CourseEnrollForm(request.POST, request.FILES, instance=course)
            if form_data.is_valid():
                form_data.save()
                messages.success(request, 'Enrollment Info Updated Successfully :)')
                return redirect('course_enroll_list')
        else:
            form_data = CourseEnrollForm(instance=course)
        context = {
            'form_data' : form_data,
            'page_title' : 'Update Course Enrollment Info',
            'form_title':'Update Course Enrollment',
            'form_btn': 'Update',
        }
        return render(request, 'master/base-form.html', context)
    else:
        return redirect('dashboard_view')


@login_required
@require_POST
def delete_enroll_info(request, id):
    if request.user.user_type == 'Admin':
        course = get_object_or_404(CourseEnrollModel, id=id)
        course.delete()
        messages.success(request, 'Enrolled Student Deleted Successfully :(')
        return redirect('course_enroll_list')
    else:
        return redirect('dashboard_view')
    
@login_required
def assign_teacher_list(request):
    if request.user.user_type == 'Admin':
        assigned_data = AssignTeacherModel.objects.all()
    elif request.user.user_type == 'Teacher':
        assigned_data = AssignTeacherModel.objects.filter(teacher__user=request.user)
    else:
        assigned_data = AssignTeacherModel.objects.none()

    context = {
        'assigned_data': assigned_data
    }
    return render(request, 'assign-teacher-list.html', context)

@login_required
def assign_new_teacher(request):
    if request.user.user_type == 'Admin':
        if request.method == 'POST':
            form_data = AssignTeacherForm(request.POST)
            if form_data.is_valid():
                form_data.save()
                messages.success(request, 'Teacher Assigned Successfully :)')
                return redirect('assign_teacher_list')
        else:
            form_data = AssignTeacherForm()
        context = {
            'form_data': form_data,
            'page_title': 'Teacher Assignment Info',
            'form_title': 'Assign Course to Teacher',
            'form_btn': 'Assign Teacher',
        }
        return render(request, 'master/base-form.html', context)
    else:
        return redirect('dashboard_view')
    
@login_required
def edit_assign_teacher_info(request, id):
    if request.user.user_type == 'Admin':
        assignment = get_object_or_404(AssignTeacherModel, id=id)
        if request.method == 'POST':
            form_data = AssignTeacherForm(request.POST, request.FILES, instance=assignment)
            if form_data.is_valid():
                form_data.save()
                messages.success(request, 'Assignment Info Updated Successfully :)')
                return redirect('assign_teacher_list')
        else:
            form_data = AssignTeacherForm(instance=assignment)
        context = {
            'form_data': form_data,
            'page_title': 'Update Teacher Assignment Info',
            'form_title': 'Update Teacher Assignment',
            'form_btn': 'Update',
        }
        return render(request, 'master/base-form.html', context)
    else:
        return redirect('dashboard_view')

@login_required
@require_POST
def delete_assign_teacher_info(request, id):
    if request.user.user_type == 'Admin':
        assignment = get_object_or_404(AssignTeacherModel, id=id)
        assignment.delete()
        messages.success(request, 'Teacher Assignment Deleted Successfully :(')
        return redirect('assign_teacher_list')
    else:
        return redirect('dashboard_view')