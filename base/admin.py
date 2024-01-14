from django.contrib import admin

from . models import Tea

class TeaAdmin(admin.ModelAdmin):
	list_display = ['Farmer_name', 'Farmer_contact', 'Farmer_id', 'Farmer_quantity', 'Amount', 'Paid']

	search_fileds = ['Farmer_name', 'Farmer_contact','Farmer_id']
admin.site.register(Tea, TeaAdmin)
