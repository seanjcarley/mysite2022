from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Volume
from django.db.models import Q

# Create your views here.
@login_required
def get_data(request):
    ''' get data from source '''
    pass



@login_required
def add_data(request):
    ''' add data to db '''
    if request.method == 'POST':
        form_add_data = {
            'epoch': request.POST['epoch'],
            'direction': request.POST['direction'],
            'station_id': request.POST['station_id'],
            'vehicle_id': request.POST['vehicle_id'],
            'event_id': request.POST['event_id'],
        }
