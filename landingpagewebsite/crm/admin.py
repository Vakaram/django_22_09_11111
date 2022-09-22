from django.contrib import admin
#надо зарегистрировать наше приложение
from .models import Order
# Register your models here.
admin.site.register(Order)