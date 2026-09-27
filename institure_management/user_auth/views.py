from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    form_data = AuthenticationForm()
    if request.method == 'POST':
        form_data = AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user:
                login(request, user)
                return redirect('dashvoard_view')
        
    context = {
        'form_data' : form_data
        
    }
    
    return render(request, 'login.html', context)

def dashboard_view(request):
    
    return render(request, 'dashboard.html')
