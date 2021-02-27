from django.shortcuts import render
from .models import *
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def all_qyestion(request):
    questions=Question.objects.all()
    user=User.objects.all()
    comment=Comment.objects.all()

    return render(request,'all_questions.html',{
        'questions':questions,
        'user':user,
        'comment':comment,
    })


def single_question(request,id):
    single=Question.objects.get(id=id)
    comment=Comment.objects.filter(comment_on_id=id)

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

    return render(request,'single_questions.html',{
       'single':single,
        'comment':comment,
    })


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Question
    template_name = 'add_questions.html'
    form_class = QuestionCreateForm
    def form_valid(self, form):
        form.instance.by_user=self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Question
    template_name = 'update_questions.html'
    form_class = QuestionCreateForm

    def form_valid(self, form):
        form.instance.by_user=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.by_user:
            return True
        else:
            return False

class QuestionDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    template_name = 'delete_question.html'
    model = Question

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.by_user:
            return True
        else:
            return False
    def get_success_url(self):
        return reverse('all_qyestion')