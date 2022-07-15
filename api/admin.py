from django.contrib import admin
from api.models import Account
from django.contrib.auth.admin import UserAdmin
class AdminModel(admin.ModelAdmin):
    list_display = ['id','email','password','username','first_name','last_name','date_joined','last_login']

admin.site.register(Account,AdminModel)
