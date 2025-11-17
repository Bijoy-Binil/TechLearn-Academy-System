from django.db import models

# Create your models here.

class Course(models.Model):
    course_name  = models.CharField(max_length=20)
    description  = models.TextField(max_length=100)
    duration     = models.CharField(max_length=100)
    course_image = models.ImageField(upload_to='course/d%/m%/Y%/')

class Trainer(models.Model):
    first_name   = models.CharField(max_length=20)
    last_name    = models.CharField(max_length=20)
    email        = models.EmailField(unique=True)
    Expertise    = models.CharField(max_length=100)
    trainer_image = models.ImageField(upload_to='trainer/d%/m%/Y%/')

class Student(models.Model):
    first_name       = models.CharField(max_length=20)
    last_name        = models.CharField(max_length=20)
    email            = models.EmailField(unique=True)
    is_active        = models.BooleanField(default=True)
    Enrolled_course  = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    trainer          = models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True,related_name="students")