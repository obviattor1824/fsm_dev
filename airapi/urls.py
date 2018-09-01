from django.urls import path
from . import views

urlpatterns = [
    path('airtable', views.air_api, name ='air_api'),
]