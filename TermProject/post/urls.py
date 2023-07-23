#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('likepost/', views.likePost, name='likepost'),
]