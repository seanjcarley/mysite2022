from django.shortcuts import render
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.
def index(request):
    ''' view to return index.html '''

    name = User.objects.all()[:1]

    context = {
        'name': name,
    }

    return render(request, 'home/index.html', context)
