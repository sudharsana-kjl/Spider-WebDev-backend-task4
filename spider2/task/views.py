from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import (
	authenticate, 
	get_user_model, 
	login, 
	logout,

	)
from .forms import UserLoginForm, UserRegistrationForm, PostForm
from .models import Post
# Create your views here.
def login_view(request):
	
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request,user)
		queryset = Post.objects.all()

		return render(request,"home.html",{'user':username,"object_list": queryset})
		
	return render (request,"loginform.html",{'form':form})

def register_view(request):
	
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request,new_user)
		return render(request,"success.html",{})


	return render (request,"registerform.html",{'form':form})

def logout_view(request):
	logout(request)
	return redirect('/task/login/')

def post_create(request):
	if request.user.is_authenticated():
		if request.user.is_staff or request.user.is_superuser:
			form = PostForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				queryset = Post.objects.all()
				return render(request, "home.html", {"object_list": queryset})
			
			return render(request, "post_form.html", {"form": form})
		else:
		   return render(request,"error.html",{})

	form = UserLoginForm(request.POST or None)
	return render(request,"loginform.html",{'form':form})

def post_detail(request, id=None):
	if request.user.is_authenticated():
		instance = get_object_or_404(Post, id=id)
		context = {
			"title": instance.title,
			"instance": instance,
		}
		return render(request, "post_detail.html", context)
	form = UserLoginForm(request.POST or None)
	return render(request,"loginform.html",{'form':form})

def post_update(request, id=None):
	if request.user.is_authenticated():
		if request.user.is_staff or request.user.is_superuser:
			instance = get_object_or_404(Post, id=id)
			form = PostForm(request.POST or None, instance=instance)
			if form.is_valid():
					instance = form.save(commit=False)
					instance.save()
					context = {
					"title": instance.title,
					"instance": instance,
					}
					return render(request, "post_detail.html", context)

			
			return render(request, "post_form.html", {"title": instance.title,"instance": instance,"form":form,})
		else:
		   return render(request,"error.html",{})
		
	form = UserLoginForm(request.POST or None)
	return render(request,"loginform.html",{'form':form})



def post_delete(request, id=None):
	if request.user.is_authenticated():
		if request.user.is_superuser:
			instance = get_object_or_404(Post, id=id)
			instance.delete()
			queryset = Post.objects.all()

			return render(request,"home.html",{"object_list": queryset})
		   
		else:
			return render(request,"error.html",{})
			
	form = UserLoginForm(request.POST or None)
	return render(request,"loginform.html",{'form':form})
	
	

