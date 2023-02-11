# appointment/urls.py
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'appointment'

urlpatterns = [
path('', views.home, name='home'),
path('appointment/', views.appointment, name='appointment'),

]
urlpatterns += staticfiles_urlpatterns()