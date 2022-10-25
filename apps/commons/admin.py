from django.contrib import admin
from .models import Gender, Language, Country


# Register your models here.
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = [
        'long_name',
        'short_name',
        'is_active',
    ]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'is_active',
    ]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'alpha2code',
        'alpha3code',
        'numeric_code',
        'phone_prefix',
        'is_active',
    ]
