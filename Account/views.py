from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationForm,LoginForm,UserForm,ProfileForm
from django.contrib import messages
from Home .models import *
from django.contrib.auth.decorators import login_required
from.models import *
from Questions.models import *
# Create your views here.

"""
def register(request):
     if request.method == 'POST':
          first_name = request.POST['first_name']
          last_name  = request.POST['last_name']
          email      = request.POST['email']
          username   = request.POST['username']
          password   = request.POST['password']
          password2  = request.POST['password2']
          if password == password2:
               User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password,
               )
     return render(request,'register.html',)
""" #طريقة 1

def register(request):  #طريقة 2
     if request.method=='POST':
         form= UserCreationForm(request.POST)
         if form.is_valid():
             new_user=form.save(commit=False)
            # username=form.cleaned_data['username']
             new_user.set_password(form.cleaned_data['password1'])
             new_user.save()
             messages.success(
                  request,f'تهانينا{new_user} لقد تمت عملية تسجيل دخولك بنجاح ')
             return redirect('profile')
     else:
       form=UserCreationForm()
     return render(request,'register.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')

        else:
            messages.warning(request ,'There is an error in the username or password')
    else:
         form=LoginForm()
    return render(request,'login.html',
                  {
               'form':form,
                  })

#طريقة 1 من خلال ال url
#طريقة 2 من خلال ال form
#الطريفة 3 من خلال صفحة html





def logout_user(request):
    logout(request)
    return render(request,'logout.html',{})


@login_required(login_url='login')
def profile(request):
    user=User.objects.all()
    profile=Profile.objects.get(user=request.user)
    art=Single_Art.objects.filter(by_user=request.user)
    question=Question.objects.filter(by_user=request.user)
    comment=Comment.objects.filter(comment_on__by_user=request.user)
    return render(request,'user/profile.html',{
          'prof':profile,
           'art':art,
           'comment':comment,
           'question':question,
        'user':user,

    })

#طريقة 1 من خلال ال url
#طريقة 2 من خلال ال form

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('profile'))
    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)

    return render(request,'user/edit_profile.html',{
         'userform':userform,
        'profileform':profileform
    })