from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('template/select/', views.template_select, name='template_select'),

    path('form/', views.resume_form, name='resume_form'),
]