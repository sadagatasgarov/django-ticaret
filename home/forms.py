from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')
    catid = forms.IntegerField()


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, label=' User Name')
    email = forms.EmailField(max_length=200, label='Email')
    first_name = forms.CharField(max_length=100, label='first name', help_text='First Name')
    last_name = forms.CharField(max_length=100, label='last name', help_text='Last Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


