from django.db import models

# Create your models here.

class user(models.Model):
	name = models.CharField(max_length = 200, null = True)
	phone = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_length = 200, null = True)
	age = models.CharField(max_length = 200, null = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name

class category(models.Model):
	groceries = models.CharField(max_length = 200, null = True)
	outsideFood = models.CharField(max_length = 200, null = True)
	coffee = models.CharField(max_length = 200, null = True)
	gas = models.CharField(max_length = 200, null = True)
	rentMorgage = models.CharField(max_length = 200, null = True)
	LivingReparis = models.CharField(max_length = 200, null = True)
	medical = models.CharField(max_length = 200, null = True)
	schoolFees = models.CharField(max_length = 200, null = True)
	shoppingElectronics = models.CharField(max_length = 200, null = True)
	shoppingFashion = models.CharField(max_length = 200, null = True)
	kitchenEquipment = models.CharField(max_length = 200, null = True)
	legalPayments = models.CharField(max_length = 200, null = True)
	childCare = models.CharField(max_length = 200, null = True)
	enjoyment = models.CharField(max_length = 200, null = True)
	creditCard = models.CharField(max_length = 200, null = True)
	petFees = models.CharField(max_length = 200, null = True)
	selfCareselfDevlopment = models.CharField(max_length = 200, null = True)
	gym = models.CharField(max_length = 200, null = True)

class statment(models.Model):
	user = models.ForeignKey(user, null = True, on_delete = models.SET_NULL)
	category = models.ForeignKey(category, null = True, on_delete = models.SET_NULL)
	dateInput = models.CharField(max_length = 200, null = True)
	termLength = models.CharField(max_length = 200, null = True)
	paycheck = models.CharField(max_length = 200, null = True)
