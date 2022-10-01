from django.urls import path
from .views import *

urlpatterns = [
    path('', manytoone, name='m2o')
]