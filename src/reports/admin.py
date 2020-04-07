from django.contrib import admin
from .models import SuspectedCase, Declared

# Register your models here.
admin.site.register([SuspectedCase, Declared])
