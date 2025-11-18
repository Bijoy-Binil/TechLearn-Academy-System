from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('courses/', views.course_list,name='course'),
    path('trainers/', views.trainer_list,name='course'),
    path('students/', views.student_list,name='course'),
]
