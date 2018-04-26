from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='标题')

    body = models.TextField(verbose_name='正文')

    created_time = models.DateTimeField(verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')

    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
