from django.contrib import admin
from .models import Hackathon

@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'start_date', 'end_date', 'max_team_size')
    list_filter = ('organizer',)
    search_fields = ('title', 'description')
