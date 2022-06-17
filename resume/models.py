from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Education(models.Model):
    ''' model holding education information '''


    class Meta:
        ''' change the table name in admin page'''
        verbose_name_plural = 'Education_Details'
  

    institute = models.CharField(max_length=75, null=False, blank=False)
    course = models.CharField(max_length=75, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.TextField(null=False, blank=False, default='')
    award = models.CharField(max_length=75, null=True, blank=True)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


class Employment(models.Model):
    ''' model holding employment details '''


    class Meta:
        ''' change the table name in admin page'''
        verbose_name_plural = 'Employment_Details'


    company = models.CharField(max_length=75, null=False, blank=False)
    position = models.CharField(max_length=75, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.TextField(null=False, blank=False, default='')
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class ExecSummary(models.Model):
    ''' model holding executive summaries '''

    class Meta:
        ''' change the table name in admin page '''
        verbose_name_plural = 'Executive_Summary'

    summary = models.TextField(null=False, blank=False, default='')
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    active = models.BooleanField(null=False, blank=False, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    
