from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('xero', views.xero_api, name ='xero_api'),
]