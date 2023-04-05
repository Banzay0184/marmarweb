from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Clients, Orders, Service, User, OrderField


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-[#EF4D23] transition duration-150 ease-in-out sm:text-sm sm:leading-5"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:shadow-outline-blue focus:border-[#EF4D23] transition duration-150 ease-in-out sm:text-sm sm:leading-5"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class ClientForm(forms.ModelForm):
    full_name = forms.CharField(label='Полное имя фамилия')
    phone = forms.IntegerField(label='Номер телефона')
    address = forms.CharField(label='адресс')
    manager = forms.SelectMultiple()
    status = forms.SelectMultiple()
    form = forms.SelectMultiple()

    class Meta:
        model = Clients
        fields = ('full_name', 'phone', 'address', 'status', 'manager', 'form')


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(parent=None)

    title = forms.CharField(label='Название заказа')
    order_number = forms.IntegerField(label='Номер заказа')
    client = forms.SelectMultiple()
    status = forms.SelectMultiple()

    class Meta:
        model = Orders
        fields = ('title', 'order_number', 'client', 'status', 'service', 'numbers', 'user')


class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Service.objects.filter(parent=None)

    name = forms.CharField()

    class Meta:
        model = Service
        fields = ('name', 'department', 'parent')


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('title', 'order_number', 'client', 'status', 'numbers', 'user')


class OrderFieldForm(forms.ModelForm):
    title = forms.CharField(label='Hujjat nomi')
    field = forms.FileField(label='Hujjat')

    class Meta:
        model = OrderField
        fields = ('title', 'field')

# class ProjectServiceForm(forms.ModelForm):
#     parcent = forms.IntegerField()
#     max_parcent = forms.IntegerField()
#
#     class Meta:
#         model = ProjectService
#         fields = ('parcent', 'max_parcent')
