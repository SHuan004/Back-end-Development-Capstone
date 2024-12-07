from django.contrib import admin

# Register your models here.
from .models import Concert


# Registrar el modelo Concert
admin.site.register(Concert)