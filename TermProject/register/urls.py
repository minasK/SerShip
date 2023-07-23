from django.urls import path
from . import views
from tasks.views import register_request, login_request, logout_request

# Create your views here.

urlpatterns = [
    path('register/', vr.register, name="register"),
    path('login/', login_request, name='login'),
    path('login/', logout_request, name='logout'),
]