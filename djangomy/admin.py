from django.contrib import admin
from .models import *
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = [ field.name  for field in Subscribers._meta.fields]
    list_display = ['name', 'email']
    # list_filter = ['name', 'email']
    search_fields = ['name', 'email']

    class Meta:
        model = Subscribers

admin.site.register(Subscribers, SubscriberAdmin)