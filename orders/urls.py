from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('created/', views.create_orders, name='create_orders'),
]