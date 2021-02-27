from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Learn(models.Model):
    title=models.CharField(max_length=300)
    content=RichTextField()
    purport=RichTextField()
    image=models.FileField()
    created_at = models.DateTimeField(auto_now=True)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Learn, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Single_Art(models.Model):
    title=models.CharField(max_length=300)
    content=RichTextField()
    image=models.FileField()
    created_at = models.DateTimeField(auto_now=True)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='Single_Arte')
    active=models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Single_Art, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name=models.CharField(max_length=300, verbose_name='Your name')
    email=models.EmailField(verbose_name='Your Email')
    content=models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    comment_on = models.ForeignKey(Single_Art,related_name='Comment_Articale', on_delete=models.CASCADE)


    def __str__(self):
        return 'Commented {} on {}'.format(self.name, self.comment_on)

    class Meta:
        ordering=('-created_at',)
        