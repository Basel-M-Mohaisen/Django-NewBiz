from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contat_me(request):
    myinfo=Info.objects.first()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'message from :' + name,
            message,
            email,
            ['bamimo1999@gmail.com'],

        )

    return render(request,'contact.html',{'myinfo':myinfo})