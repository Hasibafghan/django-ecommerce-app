from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=30, label='First Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name',
            'name': 'first_name'
        })
    )
    last_name = forms.CharField(
        max_length=30, label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name',
            'name': 'last_name'
        })
    )
    email = forms.EmailField(
        max_length=254, label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'name': 'email'
        })
    )
    username = forms.CharField(
        max_length=150, label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'name': 'username'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        # Optional: remove password field from the form
        # if 'password' in self.fields:
        #     self.fields.pop('password')


# we use widget tweaks to add bootstrap classes to the form fields
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,label='First Name' , )
    last_name = forms.CharField(max_length=30,label='Last Name' , )
    email= forms.EmailField(max_length=30,label='Email', ) # widget=forms.TextInput(attrs={class:'form-control' , 'placeholder':'Enter your username' , 'name':'username'})
    username= forms.CharField(max_length=30,label='Username' , ) 
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