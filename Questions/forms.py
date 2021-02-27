from django import forms
from.models import *


class QuestionCreateForm(forms.ModelForm):
    title=forms.CharField(label='Title')
    content=forms.CharField(label='Question',widget=forms.Textarea)

    class Meta:
        model=Question
        fields=('title','content')

