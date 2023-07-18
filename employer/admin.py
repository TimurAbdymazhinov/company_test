from django.contrib import admin

from employer.models import Employer


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

    fieldsets = [
        [None, {'fields': ['name', 'surname', 'avatar', 'position', 'salary', 'age', 'department']}],
    ]
