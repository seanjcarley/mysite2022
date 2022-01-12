from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    ''' view to return index.html '''
    return render(request, 'home/index.html')
