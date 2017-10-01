from django.contrib import admin
from .models import Table_field

class TableAdmin(admin.ModelAdmin):
    list_display = ('id','x', 'y',)
    list_editable = ('x','y',)

admin.site.register(Table_field, TableAdmin)