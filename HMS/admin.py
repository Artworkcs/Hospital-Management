from django.contrib import admin
from .models import*

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Statistic)

# Register your models here.
