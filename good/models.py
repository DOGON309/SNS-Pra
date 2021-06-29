from django.db import models
from django.contrib.auth.models import User
from post.models import PostModel

class GoodModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'good_owner')
    message_id = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name = 'message_id')