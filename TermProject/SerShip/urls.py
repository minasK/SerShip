from django.urls import path
from . import views
# Create your views here.
urlpatterns = [
    path('', views.SerShip, name='SerShip'), #in path the first arg is the url after 127..., views.index is the path to see from python and the last one is the specification of where to find the index
]