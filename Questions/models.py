from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Question(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_question',args=[self.id])

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    name=models.CharField(max_length=300, verbose_name='Your name')
    email=models.EmailField(verbose_name='Your Email')
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_on = models.ForeignKey(Question,related_name='Comment_Question', on_delete=models.CASCADE)


    def __str__(self):
        return 'Commented {} on {}'.format(self.name, self.comment_on)

    class Meta:
        ordering=('-created_at',)