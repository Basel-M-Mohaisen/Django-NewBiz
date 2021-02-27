from django.urls import path
from .views import *
urlpatterns = [
    path('contat_me',contat_me,name='contat_me'),


]