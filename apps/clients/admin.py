from django.contrib import admin

from apps.clients.models import Client


# Register your models here.
@admin.register(Client)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'firstname',
        'lastname',
        'date_of_birth',
        '_gender',
        'picture',
        '_country',
        'lang',
        'is_kid',
        'is_active',
    ]
