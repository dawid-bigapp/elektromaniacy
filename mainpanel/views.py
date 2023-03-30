from django.shortcuts import render
# from .templates.mainpanel.py import cenyHurtowe
from .forms import send_mail

def home(request):
    return render(request, 'mainpanel/html/index.html', {})

def program2(request):
    form = send_mail()
    return render(request, 'mainpanel/html/program2.html', {'form' : form})