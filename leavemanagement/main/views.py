from django.shortcuts import render
from main.forms import UserRegForm
from main.models import User
from django.contrib.auth import authenticate

# Create your views here..
def home_view(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		user = authenticate(username=data["username"], 
		password=data["password"])
		if user:
			msg="Login successfully"
		else:
			msg="Login failed"
	return render(request,"main/home.html",{"msg":msg})
def user_register(request):
	msg=""
	if request.method=="POST":
		form=UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			user_instance=form.instance 
			user_instance.set_password(user_instance.password)
			user_instance.save()
			msg="User registered successfully"
		else:
			msg=form._errors
	form=UserRegForm()
	return render(request, "main/user_register.html",
		{"form":form,"msg":msg})
