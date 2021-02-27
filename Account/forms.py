from django import forms
from django.contrib.auth.models import User
from.models import Profile

class UserCreationForm(forms.ModelForm):
    username=forms.CharField(label='Username',max_length=15)
    email    =forms.CharField(label='Email')
    first_name=forms.CharField(label='First Name',max_length=15)
    last_name=forms.CharField(label='Last Name',max_length=15)
    password1=forms.CharField(label='Password',max_length=15,widget=forms.PasswordInput(),min_length=8)
    password2=forms.CharField(label='confirm password',max_length=15,widget=forms.PasswordInput(),min_length=8)

    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password does not match.')
        return cd['password2']

    def clean_username(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('There is a registered user with this name')
        return cd['username']

class LoginForm(forms.ModelForm):
    username=forms.CharField(label='Username',max_length=15)
    password=forms.CharField(label='Password',max_length=15,widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','password')

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number', 'image', 'Specialization', 'education_level']