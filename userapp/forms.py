from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from userapp.models import Customer

class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=75, required=True)
	last_name = forms.CharField(max_length=75, required=True)
	email = forms.CharField(max_length=75, required=True)

	class Meta:
		model=User
		fields=['first_name','last_name','email','username','password1','password2',]


class RegForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude=('user',)


class EditForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your first name', 'class': 'form-control'}),required=True)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your last name', 'class': 'form-control'}),required=True)
	email=forms.EmailField(label='Email',required=True,widget=forms.TextInput(attrs={'placeholder': 'Type Your e-mail ID', 'class': 'form-control ',
			'id':'ind_email','required':'required','maxlength' : '50'}))