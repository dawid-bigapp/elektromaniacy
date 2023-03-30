from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('program2/', views.program2, name='program2'),
]
