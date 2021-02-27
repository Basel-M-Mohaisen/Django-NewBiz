from django.urls import path
from .views import *
urlpatterns = [
    path('',Home,name='Home'),
    path('learn/<str:slug>',what_i_learn, name='what'),
    path('Articles_on/<str:slug>',Single, name='Single'),
    path('Show_art/<int:id>',Show_art, name='Show_art'),

]