from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='名字')
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    url = models.URLField(blank=True, verbose_name='个人网站')
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
