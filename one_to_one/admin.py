from django.contrib import admin
from .models import Vehicle, Car
# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['owner', 'reg_no']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'vehicle']
