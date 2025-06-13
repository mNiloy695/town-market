from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User  # Import your custom user model

# admin.site.register(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # Fields to display in the user list
    list_display = ('username', 'email', 'phone', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    # Field structure in the admin detail page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'profile_img')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Custom Info'), {'fields': ('role',)}),
    )

    # Fields to use when creating a new user from admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'password1', 'password2', 'role'),
        }),
    )

    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)
