from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    ''' model holding project information '''


    class Meta:
        ''' change the table name in admin page '''
        verbose_name_plural = 'Project_Details'


    proj_name = models.CharField(max_length=75, null=False, blank=False)
    proj_type = models.CharField(max_length=50, null=False, blank=False)
    proj_description = models.TextField(null=False, blank=False)
    proj_link = models.CharField(max_length=200, null=False, blank=False)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

