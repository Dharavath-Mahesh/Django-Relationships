from django.urls import path
from . import views
urlpatterns = [
    path('', views.onetoone, name = 'o2o'),
]
