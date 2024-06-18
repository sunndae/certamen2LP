from django.contrib import admin
from backend.models import Number
# Register your models here.


class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'letter')
    search_fields = ('number', 'letter')

admin.site.register(Number, NumberAdmin)