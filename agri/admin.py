from django.contrib import admin
from .models import Faculty, Department, vips


# Register your models here

admin.site.site_header = 'UAF Admin'
admin.site.site_title = 'Hamza & Rizwan'
admin.site.index_title = 'UAF Map Navigator'


admin.site.register(Faculty)
admin.site.register(vips)

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