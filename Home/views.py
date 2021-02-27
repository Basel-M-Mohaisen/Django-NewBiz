from django.shortcuts import render,get_object_or_404
from.models import *
from Questions.models import Question
# Create your views here.

def Home(request):
    what_Learn=Learn.objects.all()
    question=Question.objects.all()
    article=Article.objects.all()
    user=User.objects.all()
    comments=Comment.objects.all()



    context = {
        'learn': what_Learn,
        'article':article,
        'user':user,
        'question':question,
        'comments':comments,
    }
    return render(request,'base.html',context)


def what_i_learn(request ,slug):
    what_i_learn = Learn.objects.get(slug=slug)
    context = {
        'what':what_i_learn,
    }
    return render(request,'base_part/what_i_learn.html',context)



def Single(request ,slug):
    artic=get_object_or_404(Article,slug=slug)
    sing=Single_Art.objects.filter(article__slug=slug ,active=True)

    context = {
        'artic': artic,
        'sing':sing,
    }
    return render(request,'base_part/Single_Art.html',context)



def Show_art(request ,id):
    if request.method == 'POST':
        c_name = request.POST['name']
        c_email = request.POST['email']
        c_content = request.POST['content']
        Comment.objects.create(
            name=c_name,
            email=c_email,
            content=c_content,
            comment_on_id=id,
        )
    show=Single_Art.objects.get(id=id)
    comments=Comment.objects.filter(comment_on_id=id,active=True)


    context = {
        'show':show,
        'comments':comments,
    }


    return render(request,'base_part/show_Art.html',context)