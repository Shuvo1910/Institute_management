from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def login_view(request):
    form_data = AuthenticationForm()
    if request.method == 'POST':
        form_data = AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user:
                login(request, user)
                messages.success(request, 'User Logged In Successfully.')
                return redirect('dashboard_view')
        messages.warning(request, 'Invalid username or password!')
    context = {
        'form_data' : form_data
        
    }
    
    return render(request, 'login.html', context)

def dashboard_view(request):
    
    return render(request, 'dashboard.html')
