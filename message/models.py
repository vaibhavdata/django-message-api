from django.db import models
from api.models import Account
# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")



    def __str__(self):
        return self.message

