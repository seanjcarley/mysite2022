from django.contrib import admin
from .models import Station, Vehicle, Event, Volume

# Register your models here.
class StationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'location',
    )

    ordering = ('id',)

class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vehicle_desc',
    )

    ordering = ('id',)

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'event_code',
        'event_desc',
    )

    ordering = ('id',)

class VolumeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'epoch',
        'direction',
        'event_id',
        'station_id',
        'vehicle_id',
    )

    ordering = ('-epoch',)


admin.site.register(Station, StationAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Volume, VolumeAdmin)