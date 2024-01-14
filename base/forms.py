from django import forms
from . models import Tea

class TeaForm(forms.Form):
	Farmer_name=forms.CharField(max_length=100)
	Farmer_contact=forms.IntegerField()
	Farmer_id = forms.CharField(max_length=30)
	Farmer_email=forms.EmailField(max_length=100)
	Farmer_quantity = forms.CharField(max_length=50)
	Amount = forms.DecimalField(max_digits=10, decimal_places=2)
	Paid = forms.CharField(max_length=20)

	Date=forms.DateTimeField()
