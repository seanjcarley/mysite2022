from django.shortcuts import render
from django.contrib.auth.models import User
from resume.models import ExecSummary
# from django.http import HttpResponse

# Create your views here.
def index(request):
    ''' view to return index.html '''

    name = User.objects.all()[:1]
    exsum = ExecSummary.objects.all()[:1]

    context = {
        'name': name,
        'summary': exsum,
    }

    return render(request, 'home/index.html', context)
