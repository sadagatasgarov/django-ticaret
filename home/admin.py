from django.contrib import admin

# Register your models here.
from home.models import Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']
