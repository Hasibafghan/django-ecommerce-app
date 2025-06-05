from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , SetPasswordForm
from django import forms


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
        if 'password' in self.fields:
            self.fields.pop('password')



class PasswordChangeForm(SetPasswordForm):
    # old_password = forms.CharField(
    #     max_length=30,
    #     label='Old Password',
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter your old password',
    #         # 'name': 'password',
    #         # 'type': 'password'
    #     })
    # )
    new_password1 = forms.CharField(
        max_length=30,
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password must be at least 8 characters',
            # 'name': 'password',
            # 'type': 'password'
        })
    )
    new_password2 = forms.CharField(
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
        fields = ( 'new_password1', 'new_password2')

class UpdateProfileForm(forms.ModelForm):
    phone = forms.CharField()
    address1 = forms.CharField()
    address2 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = User
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'zip_code', 'country')