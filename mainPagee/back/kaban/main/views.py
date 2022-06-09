from ast import Return
from audioop import reverse
from dataclasses import fields
from multiprocessing import AuthenticationError
from telnetlib import EL
from winreg import DeleteValue
from django.db.models import F

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import CardForm, ElemForm, LoginForm, UserRegistrationForm
from .forms import ColumnForm
from .forms import RegisterForm
from .models import Column, Elemet
from .models import Card
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import UpdateView, DetailView, DeleteView

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()

    if request.method == 'POST':
        form_1 = ColumnForm(request.POST)
        if form_1.is_valid():
            form_1.save()

    form = CardForm()
    form_1 = ColumnForm()
    form_2 = ElemForm()
    column = Column.objects.all()
    card = Elemet.objects.filter(num = 1)
    card_2 = Elemet.objects.filter(num = 2)
    card_3 = Elemet.objects.filter(num = 3)
    card_4 = Elemet.objects.filter(num = 4)
    return render(request, 'main/main.html', {'column': column, 'card': card, 'form': form, 'form_1': form_1, 'card_2': card_2, 'card_3': card_3, 'card_4': card_4})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            #return render(request, 'main/main.html', {'new_user': new_user})
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/reg.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return render(request, 'main/main.html', {'form': form})
                    return redirect('kaban')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

class detailView(DetailView):
    model = Elemet
    template_name = 'main/detailView.html'
    context_object_name = 'elemet'

#def change(request):
#    if request.method == 'POST':
#       form_2 = ElemForm(request.POST)
#        if form_2.is_valid():
#            form_2.save()
#            return redirect('home')
#        else:
#            form_2 = ElemForm()
#    return render(request, 'main/change.html', {'form_2': form_2})

def changePage(request):
    return render(request, 'main/change.html')

def change(UpdateView):
    model = Elemet
    template_name = 'main/change.html'

    fields = ['num']

class update(UpdateView):
    model = Elemet
    form_class = ElemForm
    template_name = 'main/change.html'
    success_url = reverse_lazy('kaban')

class delete(DeleteView):
    model = Elemet
    template_name = 'main/delete.html'
    success_url = reverse_lazy('kaban')


