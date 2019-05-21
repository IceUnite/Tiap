from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserReg

def index(request):
	return render(request, 'app/index.html')

def login(request):
	return render(request, 'app/login.html')

def registration(request):
	if request.method == "POST":
		form = UserReg(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username} успешно зарегистрирован!')
			return redirect('login')
	else:
		form = UserReg()
	return render(request, 'app/registration.html', {'form': form})
