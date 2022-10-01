
from django.urls import path
from . import views
urlpatterns = [
    path('', views.manytomany, name = 'm2m'),
]
