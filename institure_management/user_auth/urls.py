from django.urls import path
from user_auth.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('', dashboard_view, name='dashboard_view'),
    
]
