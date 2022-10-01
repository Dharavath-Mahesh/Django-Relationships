from django.db import models

# Create your models here.
#a model Car has one-to-one relationship with a model Vehicle, i.e. a car is a vehicle.

class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length = 100)

    def __str__(self):
        return self.owner

  
class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete = models.CASCADE, primary_key = True)
    car_model = models.CharField(max_length = 100)

    def __str__(self):
        return self.car_model
    
