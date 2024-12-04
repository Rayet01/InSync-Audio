from django.contrib import admin
from .models import GuestMix

@admin.register(GuestMix)
class GuestMixAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'upload_date')
