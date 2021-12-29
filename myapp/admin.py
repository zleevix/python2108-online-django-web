from django.contrib import admin
from .models import Place, Restaurant, Waiter
# Register your models here.

admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)