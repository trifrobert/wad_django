from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.


class Customer(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	first_name = models.CharField(max_length = 30, null=True)
	last_name = models.CharField(max_length = 30, null=True)
	username = models.CharField(max_length = 30, null=True)
	password1 = models.CharField(max_length = 30, null=True)
	password2 = models.CharField(max_length = 30, null=True)
	email = models.CharField(max_length = 30, null=True)
	GENDER_TYPE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
	gender = models.CharField(max_length=1, choices=GENDER_TYPE, null=True)
	phone = models.CharField(max_length = 30, null=True)
	address = models.CharField(max_length = 100, null=True)

	def __str__(self):
		return self.username

class Product(models.Model):
	name = models.CharField(max_length = 100)
	price = models.FloatField()
	quantity= models.IntegerField()
	description = models.TextField(max_length=200)
	
	def __str__(self):
		return self.name


