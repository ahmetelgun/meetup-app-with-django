from django.contrib import admin
from .models import OrganizationModel

@admin.register(OrganizationModel)
class AuthorAdmin(admin.ModelAdmin):
    pass