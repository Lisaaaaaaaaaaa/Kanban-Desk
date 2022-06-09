from .models import Card, Elemet
from .models import Column
from django.forms import CharField, EmailInput, IntegerField, ModelForm, PasswordInput, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CardForm(ModelForm):
    class Meta:
        model = Elemet
        fields = ['text']

        widgets = {
            "text": Textarea (attrs={
                'class': 'textarea',
                'placeholde': 'Введите название карточки'
            })
        }

class ColumnForm(ModelForm):
    class Meta:
        model = Column
        fields = ['title']

        widgets = {
            "title": TextInput (attrs={
                'class': 'title',
                'placeholde': 'Введите название'
            })
        }

class ElemForm(ModelForm):
    num = forms.IntegerField(label='Номер колонки',
                               widget=forms.TextInput(attrs={'class' : 'email', 'placeholder': 'Номер колонки', 'style': 'width: 35px; left: 140px;'}))                                       
    class Meta:
        model = Elemet
        fields = ('num', 'text')

        widgets = {
            "text": Textarea (attrs={
                'class' : 'email',
                'placeholde': 'Введите название карточки',
                #'style' : 'width: 200px; margin-top: -180px; margin-left: 60px'
                #'style' : 'width: 200px; margin-left: 90px; margin-bottom: 40px'
                'style' : 'height: 90px; width: 270px; border-radius: 3px; border-width: 3px; resize: none;'
            })
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'name', 'placeholder': 'Your Name *'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Your Email *'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'password', 'placeholder': 'Your Password *'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'repeatPassword', 'placeholder': 'Confirm Password *'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'name', 'placeholder': 'Введите Имя пользователя'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'password', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'repeatPassword', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Введите Имя пользователя'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'password', 'placeholder': 'Введите пароль'}))



    


        
