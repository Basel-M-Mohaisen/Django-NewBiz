from django.contrib import admin
from .models import Learn,Article,Single_Art,Comment


class lernn(admin.ModelAdmin):
    list_display = ['title','content','created_at','by_user']
    readonly_fields =['by_user']

admin.site.register(Learn,lernn)


class Articlee(admin.ModelAdmin):
    list_display = ['title','content','created_at','by_user']

admin.site.register(Article,Articlee)


class Single_Artt(admin.ModelAdmin):
    list_display = ['title','article','created_at','by_user','active']


admin.site.register(Single_Art,Single_Artt)

class Commentt(admin.ModelAdmin):
    list_display = ['name','created_at','comment_on']


admin.site.register(Comment,Commentt)