from django.shortcuts import render
from .models import Table_field

def table(request):
    set_temp = Table_field.objects.values('x', 'y')
    table_fields = []
    for e in set_temp:
        table_fields.append(e)
    return render(request, 'table/table.html', {'table_fields':table_fields})

