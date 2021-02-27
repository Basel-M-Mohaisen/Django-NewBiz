from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('register/',register,name='register'),

    #path('login/',LoginView.as_view(template_name='login.html' ),name='login'),
    path('login/',login_user, name='login'),

    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('logout/', logout_user, name='logout'),
    path('profile/',profile,name='profile'),
    path('edit_profile/',edit_profile,name='edit_profile'),

]