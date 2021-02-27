from django.urls import path
from .views import *
urlpatterns = [
    path('all_qyestion',all_qyestion,name='all_qyestion'),
    path('single_question/<int:id>',single_question, name='single_question'),
   # path('add_questions',add_question,name='add_question'),
    path('add_questions',PostCreateView.as_view(), name='add_question'),

    path('single_question/<slug:pk>/update/',PostUpdateView.as_view(), name='post_update'),
    path('single_question/<slug:pk>/delete/',QuestionDeleteView.as_view(), name='post_delete'),

]