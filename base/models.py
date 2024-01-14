from django.db import models
from django.contrib.auth.models import User

class Tea(models.Model):
	Farmer_name=models.CharField(max_length=100)
	Farmer_contact=models.IntegerField(blank=True, null=True)
	Farmer_id= models.CharField(max_length=30)
	Farmer_email=models.EmailField(max_length=100)
	Farmer_quantity = models.CharField(max_length=50)
	Amount = models.DecimalField(max_digits=10, decimal_places=2)
	Paid = models.CharField(max_length=20)
	Date=models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Tea Collection'
	

	def __str__(self):
		return self.Farmer_name
