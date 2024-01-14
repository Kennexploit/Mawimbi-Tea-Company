from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


from . forms import TeaForm
from django.contrib import messages
from . models import Tea



def home(request):
	return render(request,'base/home.html')


def login_view(request):
	
 	if request.method=='POST':
 		form = AuthenticationForm(request, data=request.POST)
 		if form.is_valid(): 
 			user = form.get_user()
 			login(request, user)
 			return redirect('/TeaCollection')
 	else: 
 		form = AuthenticationForm(request)
 		context = { "form": form}
 		return render(request, 'base/login.html', context)

def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect('/login')
	return render(request, 'base/logout.html')

	 	


def contact(request):
	return render(request, 'base/contact.html')




def about(request):
	return render(request, 'base/about.html')

def index(request):
	if not request.user.is_staff():
		return redirect('login')
	return render(request, 'base/index.html')


def register_view(request):
	form=UserCreationForm(request.POST or None)
	if form.is_valid():
		user_obj = form.save()
		return redirect('/login')
	context = {"form": form}
	return render(request, 'base/register.html', context)
 





def TeaCollection(request):
	form =TeaForm(request.POST or None)
	if form.is_valid():

		name=form.cleaned_data['Farmer_name']
		idno=form.cleaned_data['Farmer_id']
		contact=form.cleaned_data['Farmer_contact']
		mail=form.cleaned_data['Farmer_email']
		quantity=form.cleaned_data['Farmer_quantity']
		amount=form.cleaned_data['Amount']
		paid=form.cleaned_data['Paid']
		date=form.cleaned_data['Date']
	
		
 
		p = Tea(Farmer_name=name, Farmer_id=id, Farmer_contact=contact,
			Farmer_email=mail, Farmer_quantity=quantity, Paid=paid, Amount=amount, Date=date)
		p.save()
		return render(request, 'base/messages.html', {"title": "Tea Collection"})


	context = {
	"form": form,
	}	
	
	return render(request, 'base/TeaCollection.html', context)




def main(request):
	return render(request,'main.html')


















