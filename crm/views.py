from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import *
from .models import Clients, Orders, Service, Department, ProjectService, OrderField


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    return render(request, 'sign_in.html', {'form': form})


@login_required(login_url='/login_user')
def index(request):
    return render(request, 'index.html', {})


@login_required(login_url='/login_user')
def clients(request):
    clients = Clients.objects.all()
    form = ClientForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('clients')
    return render(request, 'clients.html',
                  {'clients': clients,
                   "form": form,
                   'klients_count': Clients.objects.count(),
                   })


def edit_client(request, pk):
    client = Clients.objects.get(id=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('clients')
    return render(request, 'edit_client.html',
                  {'form': form,
                   'pk': pk,
                   'client': client, })


def offic(request):
    services = Service.objects.filter(Q(parent__isnull=False))
    orders = Orders.objects.filter(user=request.user)
    departments = Department.objects.all()
    form = OrderForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()

        for i in request.POST.getlist('service'):
            services = Service.objects.filter(parent=i)

            for service in services:
                project_service = ProjectService()
                project_service.order = instance
                project_service.service = service
                project_service.parcent = 0
                project_service.max_parcent = 0
                project_service.save()
        return redirect('offic')
    return render(request, 'ofis.html',
                  {'orders': orders,
                   'departments': departments,
                   'form': form,
                   'order_count': Orders.objects.filter(is_archive=False).count(),
                   'services': services
                   })


def archive(request):
    order_archive = Orders.objects.filter(is_archive=True)
    return render(request, 'archive.html', {
        'orders': order_archive,
        'order_count': Orders.objects.filter(is_archive=True).count(),
    })


def oreders_archived(request, pk):
    order_archived = Orders.objects.filter(pk=pk)
    if order_archived.first().is_archive:
        order_archived.update(is_archive=False)
    else:
        order_archived.update(is_archive=True)

    return redirect('offic')


def edit_offic(request, pk):
    order = Orders.objects.get(id=pk)
    form = EditOrderForm(request.POST or None, instance=order)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('offic')
    return render(request, 'edit_offic.html',
                  {'order': order,
                   'form': form})


def service(request):
    services = Service.objects.all()
    form = ServiceForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.type = request.POST.get('parent')
        instance.save()
        return redirect('service')
    return render(request, 'spravitcik.html',
                  {'form': form,
                   'services': services})


def department(request, pk):
    orders = Orders.objects.get(pk=pk, user=request.user)
    order_fields = OrderField.objects.filter(order_filed_id=orders)
    form = OrderFieldForm(request.POST or None, request.FILES)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.order_filed = orders
        instance.save()
        return redirect('department', pk=pk)
    projectservices = ProjectService.objects.filter(order=orders)
    result_parcent = 0
    reuslt_sum = 0
    sum_percent = 0
    max_percent_sum = 0
    for item in projectservices:
        result_parcent += item.parcent
        reuslt_sum += item.total_prince()
        max_percent_sum += item.max_parcent
        sum_percent += (item.parcent * item.max_parcent) / 100
    return render(request, 'department.html',
                  {'orders': orders,
                   'projectservices': projectservices,
                   'order_fields': order_fields,
                   'form': form,
                   'result_parcent': result_parcent,
                   'reuslt_sum': reuslt_sum,
                   'sum_percent': sum_percent,
                   'max_percent_sum': 0 if result_parcent == 0 else int((sum_percent / result_parcent) * 100),
                   'result': reuslt_sum * max_percent_sum / 100
                   })


def sign_out(request):
    logout(request)
    return redirect('login_user')


def edit_percent(request, pk):
    project_service = {'id': pk, **request.POST}
    update = ProjectService.objects.edit(project_service)
    return redirect('department', pk=update.order.pk)
