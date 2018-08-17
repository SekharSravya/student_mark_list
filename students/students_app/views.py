from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import *
from django.db.models.functions import Cast

# Create your views here.
from .models import Subjects, Students
def index(request):
    return render(request, 'index.html')

def best_faculty(request):
    obj = Students.objects.filter(marks__gte=90).values("subject").annotate(count = Count('subject')).order_by('-count')
    sub = obj.values_list('subject',flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values("faculty")
    if obj1:
        context= {
        'heighest_count': obj1
        }
        return render(request, 'front_page.html', context)
    else:
        return HttpResponseNotFound("404 ERROR")


def best_pass_faculty(request):
    obj = Students.objects.filter(marks__gte=40).values("subject").annotate(count=Count('subject')).order_by('-count')
    sub = obj.values_list('subject', flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values("faculty")
    if obj1:
        context={'heighest_pass_count': obj1}
        return render(request, 'front_page.html', context)
    else:
        return HttpResponseNotFound("404 ERROR")

def worst_faculty(request):
    obj = Students.objects.filter(marks__lt=40).values("subject").annotate(count=Count('subject'))
    sub = obj.values_list('subject',flat=True)
    obj1 = Subjects.objects.filter(subject=sub[0]).values("faculty")
    if obj1:
        context={'heighest_fail_count':obj1}
        return render(request, 'front_page.html', context)

def best_student(request):
    obj = Students.objects.filter(marks__gte=40).values("name").annotate(total=Sum('marks')).order_by('-total')
    if obj:
        context = {'best_student':obj[0]}
        return render(request, 'front_page.html', context)

def challenger(request):
    obj = Students.objects.values("name").annotate(total=Sum('marks')).order_by('total')
    if obj:
        context = {'challenger': obj[0]}
        return render(request, 'front_page.html', context)

def best_math_student(request):
    obj = Students.objects.filter(subject = 'Mathematics').values("name").annotate(marks = Max('marks')).order_by('-marks')[:1]
    if obj:
        context = {'best_math_student':obj}
        return render(request, 'front_page.html', context)

def sub_avg(request):
    obj = Students.objects.values("subject").annotate(sub_avg = Cast(Sum('marks')/Count('subject'), FloatField()))
    if obj:
        context = {'subject': obj}
        return render(request, 'front_page.html', context)


#
