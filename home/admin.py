from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMassage


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']


@admin.register(ContactFormMassage)
class ContactFormMassageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'status', 'ip', 'note', 'create_at', 'update_at']
