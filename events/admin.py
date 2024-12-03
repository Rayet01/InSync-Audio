from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'ticket_link')
    search_fields = ('title', 'location')
    list_filter = ('date',)

admin.site.register(Event, EventAdmin)
