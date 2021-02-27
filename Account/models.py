from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
def default_place_pics():
    return "static/img/portfolio/default.png"

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile/',default=default_place_pics,null=True, blank=True)
    Specialization=models.CharField(max_length=20)
    education_level=models.CharField(max_length=20)
    city=models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE ,null=True,blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name