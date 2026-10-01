from django.shortcuts import render

def students_list(request):
    
    return render (request, 'students-list.html')
