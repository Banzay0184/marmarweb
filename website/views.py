from django.db.models import Prefetch
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    project = []
    slider = SliderHero.objects.all()
    product_images = ProjectImage.objects.all()
    projects = Projects.objects.filter(project_image__in=product_images)

    return render(request, 'home.html', {'slider': slider})


def work(request, category_id=None, page_number=1):
    project = Projects.objects.filter(category_id=category_id) if category_id else Projects.objects.all()
    categories = ProjectCategory.objects.all()
    per_page = 1
    paginator = Paginator(project, per_page)
    project_paginator = paginator.page(page_number)

    return render(request, 'work.html', {'categories': categories, 'project': project_paginator})


def project_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def about(request):
    team = Team.objects.all()
    return render(request, 'about.html', {'team': team})
