from django.contrib import admin
from .  import models
# Register your models here.

class CourceAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(models.Course,CourceAdmin)
admin.site.register(models.Trainer)
admin.site.register(models.Student)