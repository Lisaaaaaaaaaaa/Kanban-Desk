from ast import Return
from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CardForm, LoginForm, UserRegistrationForm
from .forms import ColumnForm
from .forms import RegisterForm
from .models import Column
from .models import Card
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

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
    column = Column.objects.all()
    card = Card.objects.all()
    return render(request, 'main/main.html', {'column': column, 'card': card, 'form': form, 'form_1': form_1})

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


