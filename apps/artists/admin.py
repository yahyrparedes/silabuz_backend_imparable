from django.contrib import admin

from apps.artists.models import Artist


# Register your models here.
@admin.register(Artist)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'picture',
                    'nb_album',
                    'nb_fan',
                    'radio',
                    'is_active',
                    'created_at',
                    ]
