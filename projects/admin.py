from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    ''' make the project model visible in the admin page '''

    list_display = (
        'id',
        'proj_name',
        'proj_type',
        'proj_description',
        'proj_link',
        'user_id',
    )

    # ordering = ('id',)

admin.site.register(Project, ProjectAdmin)
