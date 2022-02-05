from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    ordering = ['email']
    list_display = ('email','first_name','last_name','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','first_name','last_name')
    readonly_fields = ('id', 'date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

# Register your models here.
admin.site.register(Account,AccountAdmin)