from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'srn', 'semester', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'semester')
    search_fields = ('email', 'srn')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'srn', 'semester', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'srn', 'semester', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
