from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def projects(request):
    ''' view to return projects.html '''
    return render(request, 'projects/projects.html')

def simon(request):
    ''' view to return simon.html '''
    return render(request, 'projects/simon.html')

def mastermind(request):
    ''' view to return mastermind.html '''
    return render(request, 'projects/mastermind.html')
