from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'hackathon', 'team_name', 'registered_at')
    list_filter = ('hackathon',)
    search_fields = ('user__email', 'team_name')
