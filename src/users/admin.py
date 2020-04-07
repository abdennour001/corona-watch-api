from django.contrib import admin
from .models import User, MedicalProfile

# Register your models here.
admin.site.register([User, MedicalProfile])
