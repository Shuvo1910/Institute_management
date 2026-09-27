from django.urls import path
from user_auth.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register_view/', register_view, name='register_view'),
    path('logout_view/', logout_view, name='logout_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    
]
