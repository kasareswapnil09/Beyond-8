from django.contrib import admin
from .models import Nurse, Shift, Schedule

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_level')

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('nurse', 'shift', 'day')

admin.site.register(Nurse, NurseAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(Schedule, ScheduleAdmin)
