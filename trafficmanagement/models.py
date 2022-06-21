from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Station(models.Model):
    ''' model holding traffic station information '''

    class Meta:
        ''' change the name in the admin page '''
        verbose_name_plural = 'Stations'

    location = models.CharField(max_length=50, null=False, blank=False)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Vehicle(models.Model):
    ''' model holding vehicle type information '''

    class Meta:
        ''' change the name in the admin page '''
        verbose_name_plural = 'Vehicles'

    vehicle_desc = models.CharField(max_length=50, null=False, blank=False)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Event(models.Model):
    ''' model holding vehicle type information '''

    class Meta:
        ''' change the name in the admin page '''
        verbose_name_plural = 'Events'

    event_code = models.CharField(max_length=5, null=False, blank=False)
    event_desc = models.CharField(max_length=50, null=False, blank=False)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)


class Volume(models.Model):
    ''' model holding traffic volume information '''

    class Meta:
        ''' change the name in the admin page '''
        verbose_name_plural = 'Volumes'

    epoch = models.IntegerField(null=False, blank=False)
    direction = models.CharField(max_length=10, null=False, blank=False)
    station_id = models.ForeignKey(Station, to_field='id', on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, to_field='id', on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, to_field='id', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)
