from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from resume.models import Education, Employment, ExecSummary

# Create your views here.
def resume(request):
    ''' view to return resume.html '''

    education = Education.objects.order_by("-start_date")[:2]
    employment = Employment.objects.order_by("-start_date")[:2]
    exec_sum = ExecSummary.objects.order_by("-id")[:1]
    name = User.objects.all()[:1]
    
    context = {
        'education': education,
        'employment': employment,
        'exec_sum': exec_sum,
        'name': name,
    }

    return render(request, 'resume/resume.html', context)


def resume_all_employment(request):
    ''' view to return all employment details '''

    employment = Employment.objects.order_by("-start_date")
    name = User.objects.all()[:1]

    context = {
        'employment': employment,
        'name': name,
    }

    return render(request, 'resume/resume_emp.html', context)


def resume_all_education(request):
    ''' view to return all education details '''

    education = Education.objects.order_by("-start_date")
    name = User.objects.all()[:1]

    for i in education:
        print(i.start_date, " - ", i.end_date)

    context = {
        'education': education,
        'name': name,
    }

    return render(request, 'resume/resume_edu.html', context)

    