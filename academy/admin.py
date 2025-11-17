from django.contrib import admin
from .  import models
# Register your models here.

class CourceAdmin(admin.ModelAdmin):
    list_display = ['course_name','description','duration']

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','Expertise']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','is_active','Enrolled_course','trainer']

admin.site.register(models.Course,CourceAdmin)
admin.site.register(models.Trainer,TrainerAdmin)
admin.site.register(models.Student,StudentAdmin)