from django.contrib import admin
from .models import Registration, Team

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'hackathon', 'preferred_role', 'status', 'registered_at')
    list_filter = ('status', 'preferred_role', 'hackathon')
    search_fields = ('user__email', 'hackathon__title')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'hackathon', 'member_count', 'created_at')
    list_filter = ('hackathon',)
    search_fields = ('name', 'hackathon__title')
    filter_horizontal = ('members',)
