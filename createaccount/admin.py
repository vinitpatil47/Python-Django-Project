from django.contrib import admin
from .models import Account
# Register your models here.

admin.site.register(Account)


class AccountAdmin(admin.ModelAdmin):
    exclude = ('account_holder_name',)