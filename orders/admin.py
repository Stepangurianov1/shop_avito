from django.contrib import admin
from .models import OrderItem, Orders


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    model = Orders
