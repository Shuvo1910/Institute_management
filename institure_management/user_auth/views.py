from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    form_data = AuthenticationForm()
    # if request.method == 'POST':
        
        
    context = {
        'form_data' : form_data
        
    }
    
    return render(request, 'login.html', context)
