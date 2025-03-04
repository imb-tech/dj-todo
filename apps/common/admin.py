from django.contrib import admin
from unfold import admin as unfold




from . import models



@admin.register(models.Employee)
class EmployeeAdmin(unfold.ModelAdmin):
    list_display = ('id', 'full_name',)