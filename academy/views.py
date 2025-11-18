from django.shortcuts import render
from . models import Course,Student,Trainer
# Create your views here.

def home(request):
    total_courses_count = Course.objects.all().count()
    total_students_count = Student.objects.all().count()
    total_trainers_count = Trainer.objects.all().count()
    print(total_courses_count)
    context={
        'total_courses_count':total_courses_count,
        'total_students_count':total_students_count,
        'total_trainers_count':total_trainers_count,
    }
    return render (request,'home_page.html',context)

def course_list(request):
    courses = Course.objects.all()
    context={
        'courses':courses,

    }
    return render (request,'course_list_page.html',context)

def trainer_list(request):
    trainers = Trainer.objects.all()

    context={
        'trainers':trainers,

    }
    return render (request,'trainer_list_page.html',context)

def student_list(request):
    students = Student.objects.all()

    context={
        'students':students,

    }
    return render (request,'student_list_page.html',context)