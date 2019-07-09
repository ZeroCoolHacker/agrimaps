from django.contrib import admin
from .models import Faculty, Department


# Register your models here.

admin.site.register(Faculty)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Department'''

    list_display = (
        'name',
        'faculty',
        'map_url'
        )
    list_filter = (
        'faculty__name',
        )

    search_fields = (
        'name',
        )
    ordering = ('faculty',)