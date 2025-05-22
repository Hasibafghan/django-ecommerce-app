from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,label='First Name' , widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=30,label='Last Name' , widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email= forms.EmailField(max_length=30,label='Last Name' , widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    username= forms.CharField(max_length=30,label='Last Name' , widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password1 = forms.CharField(
        max_length=30,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password must be at least 8 characters',
            'name': 'password',
            'type': 'password'
        })
    )
    password2 = forms.CharField(
        max_length=30,
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter password',
            'name': 'password',
            'type': 'password'
        })
    )

class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')