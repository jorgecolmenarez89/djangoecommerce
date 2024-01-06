from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name','last_name', 'username', 'last_login', 'date_joined', 'is_active']
    list_display_link = ['email', 'first_name','last_name']
    readonly_fields = ['last_login', 'date_joined']
    oredering = ('-date_joined',)

    filter_horizontal = []
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)

