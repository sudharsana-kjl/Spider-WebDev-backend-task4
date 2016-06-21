from django import forms
from .models import Post
from django.contrib.auth import (authenticate, get_user_model, login, logout,)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")

			if not user.is_active:
				raise forms.ValidationError("This user is no longer active")
		return super(UserLoginForm,self).clean(*args,**kwargs) #return the default

class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput, label='Password')
	pass2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm Password')
	class Meta:
		model = User
		fields = [
		'username',
		'password',
		'pass2'
		]

	def clean_pass2(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		pass2 = self.cleaned_data.get("pass2")

		if password != pass2 :
			raise forms.ValidationError("passwords don't match")

		username_qs = User.objects.filter(username = username)
		if username_qs.exists():
			raise forms.ValidationError("Username already exists")
		return password

			#def clean_password(self):

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

		