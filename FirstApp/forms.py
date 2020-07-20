from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from FirstApp.models import *

class UserSignUpForm(UserCreationForm):
	class Meta:
		model=User
		fields=['first_name','last_name','username','password1','password2','email']




class typeoffile(ModelForm):
	class Meta:
		model=typeoffile
		fields='__all__'

class selectfileForm(ModelForm):
	class Meta:
		model=selectfile
		fields='__all__'
