from django.contrib import admin
from .models import Education, Employment, ExecSummary

# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    ''' make the education model visible in the admin page '''

    list_display = (
        'id',
        'institute',
        'course',
        'start_date',
        'end_date',
        'summary',
        'award',
        'user_id',
        'date_added',
        'last_updated',
    )

    ordering = ('-start_date',)



class EmploymentAdmin(admin.ModelAdmin):
    ''' make the employment model visible in the admin page '''

    list_display = (
        'id',
        'company',
        'position',
        'start_date',
        'end_date',
        'summary',
        'user_id',
        'date_added',
        'last_updated',
    )

    ordering = ('-start_date',)


class ExecutiveSummaryAdmin(admin.ModelAdmin):
    ''' make the Executive Summary table visible on the admin page '''

    list_display =(
        'id',
        'summary',
        'user_id',
        'active',
        'date_added',
        'last_updated',
    )


admin.site.register(Education, EducationAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(ExecSummary, ExecutiveSummaryAdmin)
