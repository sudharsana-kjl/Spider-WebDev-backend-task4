from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate, 
	get_user_model, 
	login, 
	logout,

	)
from .forms import UserLoginForm, UserRegistrationForm
# Create your views here.
def login_view(request):
	print(request.user.is_authenticated())
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request,user)
		return render(request,"home.html",{'user':username})
		print(request.user.is_authenticated())
	return render (request,"loginform.html",{'form':form})

def register_view(request):
	print(request.user.is_authenticated())
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request,new_user)


	return render (request,"loginform.html",{'form':form})

def logout_view(request):
	logout(request)
	return redirect('/task/login/')
