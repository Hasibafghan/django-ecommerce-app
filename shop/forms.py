from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# we use widget tweaks to add bootstrap classes to the form fields
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,label='First Name' , )
    last_name = forms.CharField(max_length=30,label='Last Name' , )
    email= forms.EmailField(max_length=30,label='Last Name', ) # widget=forms.TextInput(attrs={class:'form-control' , 'placeholder':'Enter your username' , 'name':'username'})
    username= forms.CharField(max_length=30,label='Last Name' , ) 
    password1 = forms.CharField(
        max_length=30,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password must be at least 8 characters',
            # 'name': 'password',
            # 'type': 'password'
        })
    )
    password2 = forms.CharField(
        max_length=30,
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter password',
            # 'name': 'password',
            # 'type': 'password'
        })
    )

class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')