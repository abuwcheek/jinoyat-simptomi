from django.contrib import admin
from .models import Crime
# Register your models here.




class CrimeAdmin(admin.ModelAdmin):
     list_display = ('name', 'category', 'common_signs')  # Admin panelda ko‘rsatiladigan maydonlar

admin.site.register(Crime, CrimeAdmin)  # Jinoyat modelini Django admin paneliga qo‘shish