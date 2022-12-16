from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


from .models import Customer
from .forms import CustomerForm, UserCreationForm
from django.http import HttpResponse

# Create your views here.

def about_us(request):
	return render(request, 'about_us.html')

def cart(request):
	return render(request, 'cart.html')

def customer_service(request):
	return render(request, 'customer_service.html')

def equipment_accessories(request):
	return render(request, 'equipment_accessories.html')

def index(request):
	return render(request,'index.html')

def instruments(request):
	return render(request, 'instruments.html')

def product1(request):
	return render(request, 'product1.html')

def register(request):

	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('sign_in.html')

	context = {'form':form}
	return render(request, 'register.html', context)

	# if request.method == 'POST':
	# 	username = request.POST['username']
	# 	password1= request.POST['password1']
	# 	password2 = request.POST['password2']
	# 	email = request.POST['email']
	

	# 	if password1 == password2:

	# 		if form.objects.filter(email=email).exists():
	# 			message.info(request, 'The email is already taken!')
	# 			return redirect('register')

	# 		elif form.objects.filter(username=username).exists():
	# 			message.info(request, 'The username is already taken!')
	# 			return redirect('register')

	# 		else:
	# 			if form.is_valid():
	# 				form.save()
	# 	else:
	# 		message.info(request, 'The password is not matching!')
	# 		return redirect('register')

	# else:
	# 	context = {'form':form}
	# 	return render(request, 'register.html', context)

def sign_in(request):
	return render(request, 'sign_in.html')