from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMassage, UserProfile


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']


class ContactFormMassageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'status', 'ip', 'note', 'create_at', 'update_at']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'city', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactFormMassage, ContactFormMassageAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
