from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMassage



class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']



class ContactFormMassageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'status', 'ip', 'note', 'create_at', 'update_at']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactFormMassage,ContactFormMassageAdmin)