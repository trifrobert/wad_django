from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Customer



class CustomerForm(ModelForm):

	class Meta:
		model = Customer
		fields = ['first_name', 'last_name', 'username','password1','password2', 'email','gender', 'phone', 'address']
		widgets = {
        'password1': forms.PasswordInput(),
        'password2': forms.PasswordInput(),
    	}

