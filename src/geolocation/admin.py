from django.contrib import admin
from .models import Location, Region, ReceptionCenter

# Register your models here.
admin.site.register([Location, Region, ReceptionCenter])
