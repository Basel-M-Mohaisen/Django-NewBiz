from django.contrib import admin
from .models import Question,Comment
# Register your models here.


class question(admin.ModelAdmin):
    list_display = ['title','created_at','by_user']

admin.site.register(Question,question)

class Commentt(admin.ModelAdmin):
    list_display = ['name','created_at','comment_on']


admin.site.register(Comment,Commentt)