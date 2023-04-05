from django.shortcuts import render
from .models import *


# Create your views here.

def Home(request):
    slider = SliderHero.objects.all()
    project = Projects.objects.all()
    return render(request, 'home.html', {'slider': slider, 'project': project})
