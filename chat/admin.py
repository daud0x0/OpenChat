from django.contrib import admin
from .models import Category, Character, Event

# Register your models here.

admin.site.register(Category)
admin.site.register(Character)
admin.site.register(Event)
