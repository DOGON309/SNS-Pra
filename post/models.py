from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'POST_owner')
    content = models.TextField(max_length=500)
    good_count = models.IntegerField(default=0)
    up_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '投稿データ'
        verbose_name_plural = '投稿データ'
        ordering = ('-up_date', )