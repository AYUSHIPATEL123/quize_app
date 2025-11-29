from django.contrib import admin
from .models import Event
# Register your models here.

# Customizing the admin interface for the Event model
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('date',)

admin.site.register(Event, EventAdmin)
