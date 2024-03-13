from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name', 'last_name',
                    'is_staff', 'is_superuser', 'is_verified', 'is_active',
                    'date_joined', 'last_login']


admin.site.register(User, UserAdmin)
