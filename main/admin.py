from django.contrib import admin
from .models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'year', 'month', 'mountains', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5',
                    'photo6')
