from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import statmentForm

# Create your views here.

def home(request, pk):
	#categorys = category.objects.first()
	#statment01 = statment.objects.get(id = pk)
	#user01 = user.objects.all()

	#var1 = statment.objects.get(id = pk)
	statment01 = statment.objects.get(id = pk)


	context = {'statment01': statment01}
	return render(request, 'accounts/dashboard.html', context)

def about(request, pk):
	statment01 = statment.objects.get(id = pk)


	context = {'statment01': statment01}
	return render(request, 'accounts/about.html', context)

def customer(request, pk):
	statment01 = statment.objects.get(id = pk)


	context = {'statment01': statment01}
	return render(request, 'accounts/customer.html', context)

def statement(request, pk):
	statment01 = statment.objects.get(id = pk)

	form = statmentForm()

	if request.method == 'POST':
		#print('Printing POST', request.POST)

		form = statmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/customer/<str:pk>/')



	context = {'statment01': statment01, 'form': form}
	return render(request, 'accounts/createStatement.html', context)

def update(request, pk):
	statment01 = statment.objects.get(id = pk)


	context = {'statment01': statment01}
	return render(request, 'accounts/updateStatement.html', context)

def login(request):
	return render(request, 'accounts/loginPage.html')

def registration(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

	if form.is_valid():
		form.save()

	context = {'form': form}
	return render(request, 'accounts/registration.html', context)
