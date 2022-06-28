from django.contrib import admin

# Register your models here.
from .models import Coffee, Suggestions

admin.site.register(Suggestions)
admin.site.register(Coffee)
