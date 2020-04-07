from django import forms
from django.forms import modelform_factory 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from league.models import UserPredictions

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class update_form(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class prof_update_form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['pic']


'''class PredictForm(forms.ModelForm):
	class Meta:
		model = UserPredictions
		fields = ['home_score', 'away_score']'''
