from django.contrib import admin
from message.models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user','message','date_created','date_updated']
admin.site.register(Message,MessageAdmin)
