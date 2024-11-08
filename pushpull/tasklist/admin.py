from django.contrib import admin
from . import models

@admin.register(models.Dist)
class DistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Dist._meta.get_fields()]
