from django.contrib import admin
from .models import *


class Infoo(admin.ModelAdmin):
    list_display = ['place','phone_number','email']

admin.site.register(Info,Infoo)