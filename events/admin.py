from django.contrib import admin
from .models import EventModel

@admin.register(EventModel)
class AuthorAdmin(admin.ModelAdmin):
    pass