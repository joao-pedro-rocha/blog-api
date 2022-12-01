from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'age', 'cpf', 'rg', 'phone', 'is_staff',
                    'is_active')

    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'age', 'cpf', 'rg', 'phone',
                       'password')
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',
            'is_active')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
