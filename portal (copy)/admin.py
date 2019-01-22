from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'pending_tasks', 'completed_tasks', 'employee_id']
    list_filter = ['date_of_joining']


admin.site.register(Employee, EmployeeAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee', 'start_date', 'deadline', 'submitted']
    list_filter = ['employee', 'submitted', 'start_date', 'deadline']

    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(employee__user=request.user)


admin.site.register(Task, TaskAdmin)
